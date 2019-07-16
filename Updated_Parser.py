### Program Object
program = {
	"title" : "",
	"style" : "",
	"difficulty" : "",
	"length" : "",
	"goal" : "",
	"notes" : "",
	"cycle" : [] 
}
day = {
		"day_name": "",
		"exercises" : [],
	}
exercise = {
		"exercise_name" : "",
		"warmup" : False,
        "order" : 0,
        "length" : "",
        "weight" : "",
        "RPE" : "",
        "Notes" : ""
	}
	
### MAIN FUNCTION
from os import path
import re
file_name = "combo.txt" 
if (path.exists(file_name) == True):
    # keeps track if we are in a cycle
    cycler = False
    # reads file
    with open(file_name) as opened_file:
        for line in opened_file:
            if (line.startswith("Title: ")):
                title = line[7:]
                program["title"] = title
                print(program["title"])
            if (line.startswith("Style: ")):
                print("FIRED")
                style = line[7:]
                program["style"] = style
                print(program["style"])
            if (line.startswith("Level: ")):
                level = line[7:]
                program["difficulty"] = level
                print(program["difficulty"])
            if (line.startswith("Length: ")):
                length = line[8:]
                program["length"] = length
                print(program["length"])
            if (line.startswith("Goal: ")):
                goal = line[6:]
                program["goal"] = goal
                print(program["goal"])
            if (line.startswith("Desc:")):
                desc = opened_file.readline()
                program["notes"] = desc
                print(program["notes"])
            if (line.startswith("-")):
                cycler = True
            if (line.startswith("Cycle")):
                cycle = {
                	"cycle_name" : "",
                	"days" : [],
                    }
                program["cycle"].append(cycle)
                
else:           
    print("""FILE NOT FOUND""")
### END MAIN
