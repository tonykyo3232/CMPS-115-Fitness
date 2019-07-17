# Helper functions

# gets the program name from a formatted line
def parse_name(program,line):
    # skips "Name: "
    program["title"] = line[6:]
    return program["title"]

# gets the style of a program from a formatted line, regardless of how many styles it has
def parse_style(program,line):
    # if it detects multiple styles, parse it
    if ("/" in line):
        styles = line.split(" / ")
        for style in styles:
            program["style"].append(style)
    else:
        # else just appends
        program["style"].append(line[7:])
    return program["style"]
#
def parse_level(program,line):
    # skips "Difficulty Level: "
    program["level"] = line[18:]
    return program["level"]

def parse_length(program,line):
    # skips "Length: "
    program["length"] = line[8:]
    return program["length"]

def parse_goals(program,line):
    # if multiple goals, parses
    if ("/" in line):
        goals = line.split(" / ")
        for goal in goals:
            program["goal"].append(goal)
    else:
        # else just appends
        program["goal"].append(line[6:])
    return program["goal"]
    
def parse_desc(program,line):
    # skips "General Info: "
    program["notes"] = line[14:]
    return program["notes"]
    
def parse_cycle_desc(cycle,line):
    # skips "Description: "
    line.split(" / ")
    cycle["cycle_name"] = line[13:]
    return cycle["cycle_name"]
    
def parse_cycle_length(cycle,line):
    # skips "Weeks: "
    cycle["length"] = line[7:]
    return cycle["length"]
# creates a cycle and parses the line for attributes 
def parse_cycle(program,line):
    cycle = {
        "cycle_name" : "n/a",
        "length" : 0,
        "days" : []
    }
    attributes = line.split(" / ")
    for attribute in attributes:
        if (attribute.startswith("Description: ")):
            parse_cycle_desc(cycle,attribute)
        if (attribute.startswith("Weeks: ")):
            parse_cycle_length(cycle,attribute)
        program["cycle"].append(cycle)
    return program["cycle"]
    
# parses the description for days
def parse_day_desc(day,line):
    # skips the "Description: " part of the line its given
    day["day_name"] = line[13:]
    return program["cycle"][-1]["days"][-1]["day_name"]

def parse_exercise_length(exercise,line):
    exercise["length"] = attribute[8:]
    return exercise["length"]

def parse_day(program,line):
    day = {
	    "day_name": "",
		"exercises" : [],
    }
    attributes = line.split(" / ")
    for attribute in attributes:
        if(attribute.startswith("Description: ")):
            day["day_name"] = attribute[13:]
            program["cycle"][-1]["days"].append(day)
    return program["cycle"][-1]["days"]

def parse_exercise_length(exercise,line):
    exercise["length"] = line[8:]
    return exercise["length"]

def parse_exercise_rpe(exercise,line):
    exercise["RPE"] = line[5:]
    return exercise["RPE"]
    
def parse_exercise_desc(exercise,line):
    # skips "Notes: "
    exercise["notes"] = line[7:]
    return exercise["notes"]
    
def parse_warmup_execise(program,line):
    exercise = {
        "exercise_name" : "n/a",
        "warmup" : True,
        "order" : 0,
        "length" : "n/a",
        "weight" : "n/a",
        "RPE" : "n/a",
        "notes" : "n/a",
    }
    attributes = line.split(" / ")
    for attribute in attributes:
        if(attribute.startswith("Exercise: ")):
            exercise["exercise_name"] = attribute[18:]
        if(attribute.startswith("Length: ")):
            parse_exercise_length(exercise,attribute)
        if(attribute.startswith("RPE: ")):
            parse_exercise_rpe(exercise,attribute)
        if(attribute.startswith("Notes: ")):
            parse_exercise_desc(exercise,attribute)
    program["cycle"][-1]["days"][-1]["exercises"].append(exercise)
    return program["cycle"][-1]["days"][-1]["exercises"]

def parse_exercise(program,line):
    exercise = {
        "exercise_name" : "n/a",
        "warmup" : False,
        "order" : 0,
        "length" : "n/a",
        "weight" : "n/a",
        "RPE" : "n/a",
        "notes" : "n/a",
    }
    attributes = line.split(" / ")
    for attribute in attributes:
        if(attribute.startswith("Exercise: ")):
            exercise["exercise_name"] = attribute[10:]
            print(exercise["exercise_name"])
        if(attribute.startswith("Length: ")):
            parse_exercise_length(exercise,attribute)
        if(attribute.startswith("RPE: ")):
            parse_exercise_rpe(exercise,attribute)
        if(attribute.startswith("General Info: ")):
            parse_exercise_desc(exercise,attribute)
    program["cycle"][-1]["days"][-1]["exercises"].append(exercise)
    return program["cycle"][-1]["days"][-1]["exercises"]
### MAIN FUNCTION
import pickle
from os import path
import re
file_name = "combo.txt" 
if (path.exists(file_name) == True):
    program = {
    	"title" : "n/a",
    	"style" : [],
    	"level" : "n/a",
    	"length" : "n/a",
    	"goal" : [],
    	"notes" : "n/a",
    	"cycle" : [] 
    }
    # reads file
    with open(file_name) as opened_file:
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
        with open('filename.pickle', 'wb') as handle:
            pickle.dump(program, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print(program)
else:
    print("NO FILE")