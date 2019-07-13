'''
[FUNCTION SPECIFICATION]
parse_exercises(lines) ::=

lines :=
===
Machine Leg Press: 5x10
Dips: 3x10/ lb: Bodyweight
...

===

return value :=
(
    exercises = [
        {
            name: "Machine Leg Press",
            desc: "5x10",
            note: ""
        },
        {
            name: "Dips",
            desc: "3x10/ lb: Bodyweight",
            note: ""

        },
        ...
    ],
    left lines = [list of line not yet handled]
)

'''
def parse_exercises(lines):
    assert len(lines) > 0

    exercises = []
    line = lines.pop(0)
    while line.strip() != "":
        print("[parse_exercises] parsing... %s" % line)
        
        tokens = line.split(":")
        if len(tokens) > 2:
            tokens = [tokens[0], ':'.join(tokens[1:])]
        tokens[1] = tokens[1].strip()

        if tokens[0].lower().strip().startswith("note"):
            assert exercise != None
            exercise["note"] = tokens[1]
        else:
            exercise = dict()
            exercise["object_type"] = "exercise"
            exercise["name"] = tokens[0]
            exercise["desc"] = tokens[1]
            exercise["note"] = ""
            exercises.append(exercise)

        line = lines.pop(0)

    return (exercises, lines)

def print_exercises(exercises):
    for exercise in exercises:
        print("%s: %s\n\tnote: %s" % (exercise["name"], exercise["desc"], exercise["note"]))

def parse_exercises_test(lines):
    print("[TEST - parse_exercises()]")
    print("[INPUT]")
    print(lines)
    print("")

    exercises, lines = parse_exercises(lines)
    print_exercises(exercises)
    print("\nLeft lines:", lines)

test_input = '''DB Press: 4x8
Machine Chest Press: 5x10
Machine Chest Flies: 3x10  
Cable Tricep Pushdown: 5x12
		Note: Use rope grip
Machine Tricep Extension: 4x12
Dips: 3x10/ lb: Bodyweight
Machine Ab Leg Curls: 4x15

a
'''.split('\n')

#parse_exercises_test(test_input)


'''
[FUNCTION SPECIFICATION]
parse_days(lines) ::=

lines :=
===
Day 1: < Day description (can be empty) >
Exercise 1: < meta >
Exercise 2: < meta >
...

Day 2: < Day description (can be empty) >
Exercise 1: < meta >

Day 3: < Day description (can be empty) >

\n (End of DAYS)
===

return value :=
(
    days = [
        {
            desc: "Legs + Shoulders",
            exercises: []
        },
        {
            desc: "Legs + Shoulders",
            exercises: []
        },
        ...
    ],
    left lines = [list of line not yet handled]
)

'''
def parse_days(lines):
    assert len(lines) > 0

    days = []
    line = lines.pop(0)
    while line.strip() != "":
        print("[parse_days] parsing... %s" % line)
        day = dict()
        day["object_type"] = "day"

        tokens = line.split(":")
        if len(tokens) > 2:
            tokens = [tokens[0], ':'.join(tokens[1:])]
        tokens[1] = tokens[1].strip()

        assert tokens[0].lower().strip().startswith("day ")

        exercises, lines = parse_exercises(lines)
        day["desc"] = tokens[1]
        day["exercises"] = exercises
        days.append(day)

        line = lines.pop(0)
    
    return (days, lines)

def print_days(days):
    for day in days:
        print("DAY: " + day["desc"])
        print_exercises(day["exercises"])
        print("")

def parse_days_test(lines):
    print("[TEST - parse_days()]")
    print("[INPUT]")
    print(lines)
    print("")

    days, lines = parse_days(lines)
    print_days(days)
    print("\nLeft lines:", lines)

test_input = '''Day 1: Legs + Shoulders
Machine Leg Press: 5x10
Machine Leg Extensions: 4x12
Machine Lying Hamstring Curls: 4x12
Calf Raises: 4x25
Barbell Shoulder Press: 4x6
Dumbbell Side Raises: 4x15
DB Front Raises: 4x15
Lying Leg Raises: 4x20

Day 2: Rest Day

Day 3: Chest + Triceps
DB Press: 4x8
Machine Chest Press: 5x10
Machine Chest Flies: 3x10  
Cable Tricep Pushdown: 5x12
		Note: Use rope grip
Machine Tricep Extension: 4x12
Dips: 3x10/ lb: Bodyweight
Machine Ab Leg Curls: 4x15


a
'''.split('\n')

#parse_days_test(test_input)


'''
[FUNCTION SPECIFICATION]
parse_cycles(lines) ::=

lines :=
===
Cycle 1: <cycle name & week count>
...

Cycle 2: <cycle name & week count>
...

===

return value :=
(
    cycles = [
        {
            desc: "something (6 weeks)",
            days: [made by parse_days() function]
        },
        {
            desc: "...",
            days: [...]
        },
        ...
    ],
    left lines = [list of line not yet handled]
)

'''
def parse_cycles(lines):
    assert len(lines) > 0

    cycles = []
    line = lines.pop(0)
    while line.strip() != "":
        print("[parse_cycles] parsing... %s" % line)
        cycle = dict()
        cycle["object_type"] = "cycle"

        tokens = line.split(":")
        if len(tokens) > 2:
            tokens = [tokens[0], ':'.join(tokens[1:])]
        tokens[1] = tokens[1].strip()

        assert tokens[0].lower().strip().startswith("cycle ")

        days, lines = parse_days(lines)
        cycle["desc"] = tokens[1]
        cycle["days"] = days
        cycles.append(cycle)

        print(lines)
        line = lines.pop(0)
    
    return (cycles, lines)

def print_cycles(cycles):
    for cycle in cycles:
        print("CYCLE: " + cycle["desc"])
        print_days(cycle["days"])
        print("")

def parse_cycles_test(lines):
    print("[TEST - parse_cycles()]")
    print("[INPUT]")
    print(lines)
    print("")

    cycles, lines = parse_cycles(lines)
    print_cycles(cycles)
    print("\nLeft lines:", lines)

test_input = '''Cycle 1: 6 weeks
Day 1: Legs + Shoulders
Machine Leg Press: 5x10
Machine Leg Extensions: 4x12
Machine Lying Hamstring Curls: 4x12
Calf Raises: 4x25
Barbell Shoulder Press: 4x6
Dumbbell Side Raises: 4x15
DB Front Raises: 4x15
Lying Leg Raises: 4x20

Day 2: Rest Day

Day 3: Chest + Triceps
DB Press: 4x8
Machine Chest Press: 5x10
Machine Chest Flies: 3x10  
Cable Tricep Pushdown: 5x12
		Note: Use rope grip
Machine Tricep Extension: 4x12
Dips: 3x10/ lb: Bodyweight
Machine Ab Leg Curls: 4x15



NEXT
'''.split('\n')

#parse_cycles_test(test_input)



def parse_prog(lines):
    assert len(lines) != 0

    prog_dict = dict()
    prog_dict["object_type"] = "program"
    cursor_key = None

    # program name (string)
    line = lines.pop(0)
    tokens = line.split(":")
    tokens = list(map(lambda token: token.strip(), tokens))
    assert tokens[0].lower() == "name"
    prog_dict["name"] = tokens[1]

    # program styles (list<string>)
    line = lines.pop(0)
    tokens = line.split(":")
    tokens = list(map(lambda token: token.strip(), tokens))
    assert tokens[0].lower() == "styles"
    prog_dict["styles"] = list(map(lambda style: style.strip(), tokens[1].split(',')))

    # program level (int)
    level_map = {
        "beginner": 0,
        "intermediate": 1,
        "advance": 2
    }
    line = lines.pop(0)
    tokens = line.split(":")
    tokens = list(map(lambda token: token.strip().lower(), tokens))
    assert tokens[0] == "level"
    prog_dict["level"] = level_map[tokens[1]]

    # program length (string: "<int> weeks")
    line = lines.pop(0)
    tokens = line.split(":")
    tokens = list(map(lambda token: token.strip().lower(), tokens))
    assert tokens[0] == "length"
    prog_dict["length"] = tokens[1]

    # program goals (list<string>)
    line = lines.pop(0)
    tokens = line.split(":")
    tokens = list(map(lambda token: token.strip(), tokens))
    assert tokens[0].lower() == "goals"
    prog_dict["goals"] = list(map(lambda style: style.strip(), tokens[1].split(',')))

    # program description
    line = lines.pop(0)
    tokens = line.split(":")
    tokens = [tokens[0].strip(), tokens[1].lstrip()]

    line = lines.pop(0)
    while not line.startswith("-------"):
        tokens[1] += line
        line = lines.pop(0)
    
    prog_dict["desc"] = tokens[1]
    
    '''
    line = lines.pop(0)
    while not line.startswith("------"):
        print("[parse_prog] parsing... %s" % line)
        tokens = []
        if not ":" in line:
            assert cursor_key != None
            prog_dict[cursor_key] += line
        else:
            tokens = line.split(":")
            if len(tokens) > 2:
                tokens = [tokens[0], ':'.join(tokens[1:])]
            tokens[1] = tokens[1].strip()
            cursor_key = tokens[0].lower()

            prog_dict[cursor_key] = tokens[1]
        
        line = lines.pop(0)
    '''
    cycles, lines = parse_cycles(lines)
    prog_dict["cycles"] = cycles
    return (prog_dict, lines)
        

import os

programs = []
directory = "programs"
for filename in os.listdir(directory):
    if filename.endswith("program.txt"):
        with open(os.path.join(directory, filename), "r") as fp:
            lines = fp.readlines()
        prog_dict, lines = parse_prog(lines)
        print(prog_dict)

        print("----------")
        print("LEFT LINES: ", lines)
        programs.append(prog_dict)
    else:
        continue

with open("programs.pickle", "wb") as fp:
    import pickle
    pickle.dump(programs, fp)


routines = [
    {
        "name": "Massive Leg Routine",
        "styles": ["General Fitness"],
        "level": 0,
        "goals": ["Build Strength", "Build Muscle"],
        "desc": "This program contains a beginner guide to building leg muscles. User can choose workout weights accordingly.",
        "warmup": [],
        "exercises": [
            {
                "name": "Barbell Back Squats",
                "length": "5x5",
                "notes": "1:30 min rest interval"
            },
            {
                "name": "Barbell Lunges",
                "length": "4x12",
                "notes": "30-45 sec rest interval"
            },
            {
                "name": "Machine Leg Press",
                "length": "4x12",
                "notes": "1 min rest interval"
            },
            {
                "name": "Machine Leg Extension",
                "length": "3x15",
                "notes": "30-45 sec rest interval"
            },
            {
                "name": "Barbell Deadlift",
                "length": "4x8",
                "notes": "1:30 min rest interval"
            },
            {
                "name": "Machine Lying Hamstring Curls",
                "length": "4x10",
                "notes": "30-45 sec rest interval"
            },
            {
                "name": "Dumbbell Calf Raises",
                "length": "3x45",
                "notes": "30 sec rest interval"
            }
        ]
    }
]

with open("routines.pickle", "wb") as fp:
    import pickle
    pickle.dump(routines, fp)