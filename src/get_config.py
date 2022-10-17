# Imports
import toml
import os

# Configurations
class Config:
    def __init__(self, file_name):
        self.data = toml.load(os.getcwd() + f"\\{file_name}")
        self.constants = self.data["constants"]

