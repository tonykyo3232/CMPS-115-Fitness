import pickle
import os
import argparse

# Helper functions

# check whether the given token is invalid (current: "n/a" means invalid)
def is_invalid_token(token):
    return token.strip().lower().startswith("n/a")

# gets the program name from a formatted line
def parse_name(program,line):
    # skips "Name: "
    program["name"] = line[6:].strip()
    return program["name"]

# gets the style of a program from a formatted line, regardless of how many styles it has
def parse_style(program,line):
    # if it detects multiple styles, parse it
    line = line.split(":")[1].strip()
    if (" / " in line):
        styles = line.split(" / ")
        for style in styles:
            program["styles"].append(style.strip())
    else:
        # else just appends
        program["styles"].append(line)
    return program["styles"]

def parse_level(program,line):
    # skips "Difficulty Level: "
    level_map = {
        "beginner": 0,
        "intermediate": 1,
        "advance": 2
    }
    program["level"] = level_map[line.split(":")[1].strip().lower()]
    return program["level"]

def parse_length(program,line):
    # skips "Length: " "6 weeks" ["6", "weeks"]
    week_token = line[8:].split(" ")[0]
    if ( week_token.isnumeric()):
        program["length"] = int(week_token)
    else:
        program["length"] = -1
    return program["length"]

def parse_goals(program,line):
    # if multiple goals, parses
    line = line.split(":")[1].strip()
    if ("/" in line):
        goals = line.split(" / ")
        for goal in goals:
            program["goals"].append(goal.strip())
    else:
        # else just appends
        program["goals"].append(line)
    return program["goals"]
    
def parse_desc(program,line):
    # skips "General Info: "
    program["desc"] = line[14:]
    return program["desc"]
    
def parse_cycle_desc(cycle,line):
    # skips "Description: "
    cycle["desc"] = line[13:].strip()
    if is_invalid_token(cycle["desc"]):
        cycle["desc"] = ""
    return cycle["desc"]
    
def parse_cycle_length(cycle,line):
    # skips "Weeks: "
    if ( line[7:].strip().isnumeric()):
        cycle["length"] = int(line[7:].strip())
    else:
        cycle["length"] = -1
    return cycle["length"]
    
# creates a cycle and parses the line for attributes 
def parse_cycle(program,line):
    cycle = {
        "desc" : "",
        "length" : 0,
        "days" : []
    }
    attributes = line.split(" / ")
    for attribute in attributes:
        if (attribute.startswith("Description: ")):
            parse_cycle_desc(cycle,attribute)
        if (attribute.startswith("Weeks: ")):
            parse_cycle_length(cycle,attribute)
    program["cycles"].append(cycle)
    return program["cycles"]
    
# parses the description for days
def parse_day_desc(day,line):
    # skips the "Description: " part of the line its given
    day["desc"] = line[13:]
    if is_invalid_token(day["desc"]):
        day["desc"] = ""
    return program["cycles"][-1]["days"][-1]["desc"]

def parse_equipment(exercise,line):
    # skips 'Equipment: '
    machines = line[11:].split(",")
    for equipment in machines:
        exercise["equipment"].append(equipment.strip())
    return exercise["equipment"]
    

def parse_day(program,line):
    day = {
	    "desc": "",
		"exercises" : [],
		"warmup_exercises" : [],
		"recent_exercise" : None,
        "is_rest": False
    }
    attributes = line.split(" / ")
    for attribute in attributes:
        if(attribute.startswith("Description: ")):
            day["desc"] = attribute[13:].strip()
            if day["desc"].lower().startswith("rest day"):
                day["is_rest"] = True
            elif is_invalid_token(day["desc"]):
                day["desc"] = ""
    program["cycles"][-1]["days"].append(day)
    return program["cycles"][-1]["days"]

def parse_exercise_length(exercise,line):
    exercise["length"] = line[8:]
    if is_invalid_token(exercise["length"]):
        exercise["length"] = ""
    return exercise["length"]

def parse_exercise_rpe(exercise,line):
    exercise["rpe"] = line[5:]
    if is_invalid_token(exercise["rpe"]):
        exercise["rpe"] = ""
    return exercise["rpe"]
    
def parse_exercise_desc(exercise,line):
    # skips "notes: "
    tokens = line.split(":")
    if len(tokens) > 2:
        tokens = [tokens[0], ':'.join(tokens[1:])]
    note = tokens[1].strip()
    exercise["notes"].append(note)
    return exercise["notes"]
    
def parse_exercise_url(exercise,line):
    exercise["url"] = line[4:].strip()
    return exercise["url"]
 
def parse_warmup_execise(program,line):
    warmup_exercise = {
        "name" : "",
        "equipment": [],
        "length" : "",
        "weight" : "",
        "rpe" : "",
        "notes" : [],
        "url" : ""
    }
    attributes = line.split(" / ")
    if len(attributes) == 1:
        # not existing exercise 
        return []
    for attribute in attributes:
        if(attribute.startswith("Exercise: ")):
            exercise["name"] = attribute[18:]
        elif(attribute.startswith("Length: ")):
            parse_exercise_length(warmup_exercise,attribute)
        elif(attribute.startswith("RPE: ")):
            parse_exercise_rpe(warmup_exercise,attribute)
        elif(attribute.startswith("Notes: ")):
            parse_exercise_desc(warmup_exercise,attribute)
        elif(attribute.startswith("Equipment: ")):
            parse_equipment(warmup_exercise,attribute)
        elif(attribute.startswith("URL: ")):
            parse_exercise_url(warmup_exercise,attribute)
        else:
            warmup_exercise["notes"].append(attribute)
    program["cycles"][-1]["days"][-1]["warmup_exercises"].append(warmup_exercise)
    return program["cycles"][-1]["days"][-1]["warmup_exercises"]

def parse_exercise(program,line):
    exercise = {
        "name" : "",
        "equipment": [],
        "length" : "",
        "weight" : "",
        "rpe" : "",
        "notes" : [],
        "url" : ""
    }
    attributes = line.split(" / ")
    for attribute in attributes:
        if(attribute.startswith("Exercise: ")):
            exercise["name"] = attribute[10:]
        elif(attribute.startswith("Length: ")):
            parse_exercise_length(exercise,attribute)
        elif(attribute.startswith("RPE: ")):
            parse_exercise_rpe(exercise,attribute)
        elif(attribute.startswith("Notes: ")):
            parse_exercise_desc(exercise,attribute)
        elif(attribute.startswith("Equipment: ")):
            parse_equipment(exercise,attribute)
        elif(attribute.startswith("URL: ")):
            parse_exercise_url(exercise,attribute)
        else:
            exercise["notes"].append(attribute)
    program["cycles"][-1]["days"][-1]["exercises"].append(exercise)
    return program["cycles"][-1]["days"][-1]["exercises"]

### MAIN FUNCTION
def parse_file(file_path):  
    program = {
        "name" : "",
        "styles" : [],
        "level" : 0,
        "length" : 0,
        "goals" : [],
        "desc" : "",
        "cycles" : [] 
    }

    with open(file_path) as opened_file:
        for line in opened_file:
            if (line.startswith("Name: ")):
                parse_name(program,line)
            if (line.startswith("Style: ")):
                parse_style(program,line)
            if (line.startswith("Level: ")):
                parse_level(program,line)
            if (line.startswith("Length: ")):
                parse_length(program,line)
            if (line.startswith("Goal: ")):
                parse_goals(program,line)
            if (line.startswith("General Info: ")):
                parse_desc(program,line)
            if (line.startswith("Cycle: ")):
                parse_cycle(program,line)
            if (line.startswith("Day: ")):
                parse_day(program,line)
            if (line.startswith("Warm Up Exercise: ")):
                parse_warmup_execise(program,line)
            if (line.startswith("Exercise: ")):
                parse_exercise(program,line)
    return program

def parse(file_name, dir_name="./", pickle_name="", is_routine=None, next_id=0):
    if not os.path.exists(dir_name):
        print("Wrong directory")
        return

    programs = []

    if file_name == "*":
        # parse all files in the directory
        for file_name in os.listdir(dir_name):
            program = parse_file(os.path.join(dir_name, file_name))
            program["is_default"] = True
            program["_id"] = next_id
            next_id += 1
            if is_routine == None:
                # If program's type (program / routine) is not specified by argument,
                # check the type from file name
                program["is_routine"] = "routine.txt" in file_name.lower()
            else:
                program["is_routine"] = is_routine
            print(program)
            programs.append(program)
    else:
        # parse a single file
        file_path = os.path.join(dir_name, file_name)
        if not os.path.exists(file_path):
            print("Wrong file path: %s" % (file_path))
            return
        program = parse_file(file_path)
        program["is_default"] = True
        program["_id"] = next_id
        next_id += 1
        if is_routine == None:
            # If program's type (program / routine) is not specified by argument,
            # check the type from file name
            program["is_routine"] = "routine.txt" in file_name.lower()
        else:
            program["is_routine"] = is_routine
        print(program)
        programs.append(program)
    
    if pickle_name != "":
        with open(pickle_name, "wb") as fp:
            pickle.dump(programs, fp)
    return programs

if __name__ == "__main__":
    usage = '''
        python3 this_script.py --filename="Workout Dataset/programs/Combo Program.txt"
        python3 this_script.py --filename="Workout Dataset/programs/Combo Program.txt" --picklename="programs_pickle"
        python3 this_script.py --filename="Combo Program.txt" --dirname="Workout Dataset/programs/"
        python3 this_script.py --filename="*" --dirname="Workout Dataset/programs/"
        # python3 this_script.py --filename="*" --dirname="Workout Dataset/routines/"
    '''
    parser = argparse.ArgumentParser(description=usage)

    parser.add_argument('--filename', required=True)
    parser.add_argument('--dirname', required=False, default='./')
    parser.add_argument('--picklename', required=False, default='programs_pickle')

    args = parser.parse_args()

    programs = parse(args.filename, args.dirname, args.picklename)
