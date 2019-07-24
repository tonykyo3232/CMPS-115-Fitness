import pickle
import os
import argparse

# Helper functions
def parse_equipment(metadata,line):
    # skips 'Equipment: '
    machines = line[11:].split(" / ")
    for equipment in machines:
        metadata["exercises"][-1]["equipment"].append(equipment.strip())
        if (equipment not in metadata["unique_equipment"] and equipment is not "n/a"):
            metadata["unique_equipment"].append(equipment.strip())
    return metadata
    
def parse_exercise_desc(metadata,line):
    # skips "Description: "
    line = line.strip()
    line = line[13:].split(" / ")
    for sentence in line:
        metadata["exercises"][-1]["notes"].append(sentence)
    return metadata
    
def parse_exercise_url(metadata,line):
    metadata["exercises"][-1]["url"] = line[4:].strip()
    return metadata

def parse_exercise(metadata,line):
    exercise = {
        "name" : "",
        "equipment": [],
        "notes" : [],
        "url" : ""
    }
    exercise["name"] = line[10:].strip()
    exercise["_id"] = len(metadata["exercises"])
    metadata["exercises"].append(exercise)
    return metadata

### MAIN FUNCTION
def parse_howto_file(file_path="../Workout Dataset/How-To's Template.txt"):
    # creates an array of exercises
    metadata = {
        "exercises" : [],
        "unique_equipment" : []
    }
    # reads file
    with open(file_path) as opened_file:
        for line in opened_file:
            if (line.startswith("Exercise: ")):
                parse_exercise(metadata,line)
            if (line.startswith("Equipment: ")):
                parse_equipment(metadata,line)
            if (line.startswith("Description: ")):
                parse_exercise_desc(metadata,line)
            if (line.startswith("URL: ")):
                parse_exercise_url(metadata,line)
    return metadata
    
if __name__ == "__main__":
    parse_howto_file()