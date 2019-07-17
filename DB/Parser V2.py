# Helper functions

# gets the program name from a formatted line
def parse_name(program,line):
    program["title"] = line[7:]
    return program["title"]

# gets the style of a program from a formatted line, regardless of how many styles it has
def parse_style(program,line):
    if ("/" in line):
        line.split(" / ")
        for goal in line:
            program["goal"].append(goal)
    return program["goal"]

def parse_level(program,line):
    program["level"] = line[7:]
    return program["level"]

def parse_length(program,line):
    program["length"] = line[8:]
    return program["length"]

def parse_goals(program,line):
    if ("/" in line):
        line[6:].split(" / ")
        for goal in line:
            program["goal"].append(goal)
    else:
        program["goal"].append(line[6:])
    return program["goal"]
    
def parse_desc(program,line):
    desc = opened_file.readline()
    program["notes"] = desc
    return program["notes"]
    
def parse_cycle_desc(cycle,line):
    cycle["cycle_name"] = line[13:]
    return cycle["cycle_name"]
    
def parse_cycle_length(cycle,line):
    cycle["length"] = line[7:]
    return cycle["length"]

def 

def parse_cycle(program,line):
    cycle = {
        "cycle_name" : "",
        "length" : 0,
        "days" : []
    }
    attributes = line.split(" / ")
    for attribute in attributes:
        if (attribute.startswith("Description: ")):
            parse_cycle_desc(cycle,line)
        if (attribute.startswith("Weeks: ")):
            parse_cycle_length(cycle,line)
        program["cycle"].append(cycle)
    return
# parses the description for days
def parse_day_desc(day,line):
    # skips the "Description: " part of the line its given
    day["day_name"] = line[13:]
    return program["cycle"][-1]["days"][-1]["day_name"]

def parse_day((program,line)):
    day = {
	    "day_name": "",
		"exercises" : [],
    }
    attributes = line.split(" / ")
    for attribute in attributes:
        if(attribute.startswith("Description: ")):
            day["day_name"] = attribute[13:]
            program["cycle"][-1]["days"].append(day)
    return 
### MAIN FUNCTION
from os import path
import re
file_name = "combo.txt" 
if (path.exists(file_name) == True):
    program = {
    	"title" : "",
    	"style" : [],
    	"level" : "",
    	"length" : "",
    	"goal" : [],
    	"notes" : "",
    	"cycle" : [] 
    }
    # keeps track if we are in a cycle
    cycler = False
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
                day = {
		            "day_name": "",
		            "exercises" : [],
	            }
                features = line.split(" / ")
                for attribute in features:
                    if(attribute.startswith("Description: ")):
                        day["day_name"] = attribute[13:]
                program["cycle"][-1]["days"].append(day)
                print(program["cycle"][-1]["days"])
            if (line.startswith("Warm Up Exercise: ")):
                exercise = {
            		"exercise_name" : "n/a",
            		"warmup" : True,
                    "order" : 0,
                    "length" : "n/a",
                    "weight" : "n/a",
                    "RPE" : "n/a",
                    "notes" : "n/a",
                }
                features = line.split(" / ")
                exercise["exercise_name"] = line[18:]
                for attribute in features:
            	    if(line.startswith("Length: ")):
            	        exercise["length"] = attribute[8:]
            	    if(line.startswith("RPE: ")):
            	        exercise["RPE"] = attribute[5:]
            	    if(line.startswith("Notes: ")):
            	        exercise["notes"] = attribute[7:]
                program["cycle"][-1]["days"][-1]["exercises"].append(exercise)
            if (line.startswith("Exercise: ")):
                exercise = {
            		"exercise_name" : "n/a",
            		"warmup" : False,
                    "order" : 0,
                    "length" : "n/a",
                    "weight" : "n/a",
                    "RPE" : "n/a",
                    "notes" : "n/a",
                }
                features = line.split(" / ")
                exercise["exercise_name"] = line[10:]
                for attribute in features:
            	    if(line.startswith("Length: ")):
            	        exercise["length"] = attribute[8:]
            	    if(line.startswith("RPE: ")):
            	        exercise["RPE"] = attribute[5:]
            	    if(line.startswith("Notes: ")):
            	        exercise["notes"] = attribute[7:]
                program["cycle"][-1]["days"][-1]["exercises"].append(exercise)
    
else:
    print("NO FILE")