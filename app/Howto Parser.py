import pickle
import os
import argparse

# Helper functions
def parse_equipment(exercises,unique_equipment,line):
    # skips 'Equipment: '
    machines = line[11:].split(", ")
    for equipment in machines:
        exercises[-1]["equipment"].append(equipment.strip())
        if (equipment not in unique_equipment and equipment is not "n/a"):
            unique_equipment.append(equipment.strip())
    return unique_equipment
    
def parse_exercise_desc(exercises,line):
    # skips "Description: "
    line = line.strip()
    line = line[13:].split(" / ")
    for sentence in line:
        exercises[-1]["notes"].append(sentence)
    return exercises[-1]["notes"]
    
def parse_exercise_url(exercises,line):
    exercises[-1]["url"] = line[4:].strip()
    return exercises[-1]["url"]

def parse_exercise(exercises,line):
    exercise = {
        "name" : "",
        "equipment": [],
        "notes" : [],
        "url" : ""
    }
    exercise["name"] = line[10:].strip()
    exercises.append(exercise)
    return exercises

### MAIN FUNCTION
def parse_file(file_path):
    # creates an array of exercises
    exercises = []
    # finds all unique equipment and returns it for specific filtering pages
    unique_equipment = []
    # reads file
    with open(file_path) as opened_file:
        for line in opened_file:
            if (line.startswith("Exercise: ")):
                parse_exercise(exercises,line)
            if (line.startswith("Equipment: ")):
                parse_equipment(exercises,unique_equipment,line)
            if (line.startswith("Description: ")):
                parse_exercise_desc(exercises,line)
            if (line.startswith("URL: ")):
                parse_exercise_url(exercises,line)
    print(exercises)
    return exercises

def main():
    usage = '''
        python3 this_script.py --filename="Workout Dataset/programs/Combo Program.txt"
        python3 this_script.py --filename="Combo Program.txt" --dirname="Workout Dataset/programs/"
        python3 this_script.py --filename="*" --dirname="Workout Dataset/programs/"
        # python3 this_script.py --filename="*" --dirname="Workout Dataset/routines/"
    '''
    parser = argparse.ArgumentParser(description=usage)

    parser.add_argument('--filename', required=True)
    parser.add_argument('--dirname', required=False, default='./')

    args = parser.parse_args()

    #file_name = "Workout Dataset/routines/Big Arm Routine.txt" 
    file_name_input = args.filename
    dir_name_input = args.dirname
    
    if not os.path.exists(dir_name_input):
        print("Wrong directory")
        return

    programs = []
    if file_name_input == "*":
        for file_name in os.listdir(dir_name_input):
            programs.append(parse_file(os.path.join(dir_name_input, file_name)))
    else:
        file_path = os.path.join(dir_name_input, file_name_input)
        if not os.path.exists(file_path):
            print("Wrong file path: %s" % (file_path))
            return
        programs.append(parse_file(file_path))
    
    with open("programs.pickle", "wb") as fp:
        pickle.dump(programs, fp)

if __name__ == "__main__":
    main()

