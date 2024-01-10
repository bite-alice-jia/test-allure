import json
import os
from datetime import datetime


# Define a comparison function to extract timestamps from strings and convert them to datetime objects for comparison
def compare_timestamp(item):
    timestamp_str = item.split("-")[-1]
    return datetime.strptime(timestamp_str, "%Y%m%d%H%M%S")


current_directory = os.path.dirname(os.path.realpath(__file__))
directories = [folder for folder in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, folder))]
directories = [folder for folder in directories if '.' not in folder]

# Organize folders into a dictionary based on test types
organized_directories = {}
for directory in directories:
    sub_folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
    sub_folders = sorted(sub_folders, key=compare_timestamp, reverse=True)
    organized_directories[directory] = sub_folders

# Create the final data structure
directory_data = {
    "directories": [organized_directories]
}

with open("directories.json", "w") as json_file:
    json.dump(directory_data, json_file, indent=2)

print("directories.json updated successfully")
