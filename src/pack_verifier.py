# Imports
import json

# Constants
_DUMMY_PRIMARY = {
    "player_limit": int,
    "die_faces": int,
    "grid_height": int,
}

_FAIL = BaseException

# Verifier
class PackVerifier:
    @staticmethod
    def question_expect(question, location_name):
        if not isinstance(question["question"], str):
            return False, f"invalid type for \"question\" key (expected str, but received {type(question)})"
        elif "answers" not in question:
            return False, f"no answers for a question for a \"{location_name}\" location"
        elif not PackVerifier.list_expect(question["answers"], str):
            return False, "answers must all be strings"
        return True, "check complete"

    @staticmethod
    def list_expect(data_list, type_):
        for val in data_list:
            if not isinstance(val, type_):
                return False
        return True

    @staticmethod
    def verify(pack_full_path, version_indicator):
        try:
            # Opening pack
            pack_data = json.load(open(pack_full_path, encoding="utf-8"))

            # Checking for metadata
            if "meta" not in pack_data:
                raise _FAIL(f"no metadata")

            for meta_val in pack_data["meta"]:
                if type(meta_val) is not str:
                    raise _FAIL(f"invalid \"meta_val\" metadata type")
                elif meta_val.strip() == "":
                    raise _FAIL(f"empty \"meta_val\" metadata")

            # Checking versioning
            pack_version = pack_data["meta"]["version"].split("-")
            if pack_version[0] != str(version_indicator):
                raise _FAIL(f"outdated version (indicator: {pack_version[0]}, version: {pack_version[1]})")

            # Checking int data
            for val in _DUMMY_PRIMARY:
                if val not in pack_data:
                    raise _FAIL(f"missing \"{val}\" key")
                elif not isinstance(pack_data[val], int):
                    raise _FAIL(
                        f"invalid type for \"{val}\" key (expected int, but received {type(pack_data[val])})")
                elif pack_data[val] <= 0:
                    raise _FAIL(f"value \"{val}\" must be positive and nonzero")

            # Checking locations key and insides
            if "locations" not in pack_data:
                raise _FAIL(f"no \"locations\" key")

            for val in ["snakes", "ladders"]:
                if val not in pack_data["locations"]:
                    raise _FAIL(f"no \"{val}\" key inside \"locations\"")

            # Checking snakes and ladders (pun not intended I swear oh my god)
            for location_name in ["snakes", "ladders"]:
                if not isinstance(pack_data["locations"][location_name], list):
                    # Checking value correctness
                    raise _FAIL(f"invalid type for \"{location_name}\" key (expected list, but received {type(pack_data['locations'][location_name])})")

                for location in pack_data["locations"][location_name]:
                    # Checking coordinates
                    coordinates = location["coords"]
                    if not PackVerifier.list_expect(coordinates, list):
                        raise _FAIL(f"invalid coordinate type for a \"{location_name}\" location")
                    elif len(coordinates) != 2:
                        raise _FAIL(f"must have 2 coordinate values")
                    elif any(len(x) != 2 for x in coordinates) or (not any(PackVerifier.list_expect(x, int) for x in coordinates)):
                        raise _FAIL(f"invalid coordinates for a \"{location_name}\" location")

                    # Checking questions
                    if "questions" not in location:
                        raise _FAIL(f"no \"questions\" key for a \"{location_name}\" location")
                    for question in location["questions"]:
                        # 3 for loops. I should retire
                        # if you want to put this on r/programminghorror then you have my permission
                        if "question" not in question:  # Ridiculous
                            raise _FAIL(f"no question for a \"{location_name}\" location")
                        elif not (check_result:=PackVerifier.question_expect(question, location_name))[0]:
                            raise _FAIL(check_result[1])

            # Checking redemption points (someone kill me)
            if "redemption_points" not in pack_data["locations"]:
                raise _FAIL("no redemption points")

            redemption_points_data = pack_data["locations"]["redemption_points"]
            for val in ["coordinates", "points_amount", "questions"]:
                if val not in redemption_points_data:
                    raise _FAIL(f"no \"{val}\" key inside \"redemption_points\"")
                elif not PackVerifier.list_expect(redemption_points_data["coordinates"], list):
                    raise _FAIL(
                        f"invalid type for \"coordinates\" key (expected list, but received {type(redemption_points_data['coordinates'])})")
                elif not any(PackVerifier.list_expect(x, int) for x in redemption_points_data["coordinates"]):
                    raise _FAIL(f"invalid coordinates for a redemption point")
                elif redemption_points_data["points_amount"] != len(redemption_points_data["coordinates"]):
                    raise _FAIL(f"specified amount of points must be correct")

                for question in redemption_points_data["questions"]:
                    if not (check_result := PackVerifier.question_expect(question, "redemption points"))[0]:
                        raise _FAIL(check_result[1])

            # The check is now complete (thank the skies)
            return True, "check complete"
        except json.JSONDecodeError as jde:
            return False, f"JSON loading exception thrown: {jde}"

        except _FAIL as be:
            return False, be

