# Imports
import os
import json

# Detection function
def detect():
    file_names = [x for x in os.listdir(os.getcwd() + "\\packs\\") if x.endswith((".json"))]
    opened_files = [json.load(open(os.getcwd() + "\\packs\\" + x)) for x in file_names]
    pack_names = [x["meta"]["name"] for x in opened_files]
    pack_authors = [x["meta"]["author"] for x in opened_files]
    pack_descriptions = [x["meta"]["description"] for x in opened_files]
    return tuple(zip(file_names, pack_names, pack_authors, pack_descriptions))

def get_zipped():
    return [{
        "name": x[1],
        "author": x[2],
        "description": x[3]
    } for x in detect()]
