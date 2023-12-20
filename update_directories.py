import json
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
sibling_folders = [folder for folder in os.listdir(current_directory) if os.path.isdir(folder)]
directories = [folder for folder in sibling_folders if 'report' in folder]
directory_data = {
    "directories": sibling_folders
}

with open("directories.json", "w") as json_file:
    json.dump(directory_data, json_file, indent=2)

print("directories.json updated successfully")
