# ----- [START] Helper Functions for Programs/Routines Filtering -----
def level_to_string(level):
    level_map = {
        0: "Beginner",
        1: "Intermediate",
        2: "Advance"
    }
    if not level in level_map.keys():
        return "n/a"
    else:
        return level_map[level]
    

def filter_styles(program_styles, style_opt):
    if style_opt == "":
        return True

    for style in program_styles:
        if style_opt.lower() in style.lower():
            return True
    return False

def filter_goals(program_goals, goal_opt):
    if goal_opt == "":
        return True

    for goal in program_goals:
        if goal_opt.lower() in goal.lower():
            return True
    return False

# PROGRAM_LEVEL, LEVEL: 1  (meaning "intermediate")
def filter_level(program_level, level):
    if level == -1:
        # Do not filter by level if LEVEL == -1 (default)
        return True
    return program_level == level


# Note: PROGRAM_LEN := int expression for program length in weeks (ex. 4 == 4 weeks)
def filter_length(program_len, len_min, len_max):
    if len_min != -1 and len_min > program_len:
        return False
    if len_max != -1 and len_max < program_len:
        return False
    return True


def filter_program(program, style="", goal="", level=-1, len_min=-1, len_max=-1): 
    return filter_styles(program["styles"], style) \
            and filter_goals(program["goals"], goal) \
            and filter_level(program["level"], level) \
            and filter_length(program["length"], len_min, len_max)

test_program = {
    "name": "My Beginner Program",
    "styles": ["General Fitness"],
    "level": 0,
    "length": 6,
    "goals": ["Build Muscle"],
    "cycles": []
}  
test_opt = {
    "style": "General Fitness",
    "level": 0,
    "len_min": 4,
    "len_max": 8,
    "goal": "Build Muscle"
}

assert True == filter_program(test_program, test_opt["style"], test_opt["goal"], test_opt["level"], test_opt["len_min"], test_opt["len_max"])


'''
[SPEC] filter_programs

INPUT:
    program set PROGRAMS :=
    [
        // Set of Program where we want to find programs satisfying a filtering option
    ]
    filtering option OPT :=
    {
        // NOTICE: All of below attributes should be given
        // Default: "Don't filter with this attribute"
        style : "Bodybuilding",         // Default = "" 
        goal  : "Build Muscle",         // Default = ""
        len_min: 1,                  // Default = -1
        len_max: 4,                  // Default = -1
        level : 1  (== "Intermediate")  // Default = -1
    }

OUTPUT:
    SAT_PROGRAMS :=
    [
        // Programs that satisfy the given filtering option
    ]
'''
def filter_programs(programs, opt):
    sat_programs = []
    
    for program in programs:
        if filter_program(program, opt["style"], opt["goal"],
                opt["level"], opt["len_min"], opt["len_max"]):
            sat_programs.append(program)
    return sat_programs

assert [test_program] == filter_programs([test_program], test_opt)
        


def filter_routine(routine, style="", goal="", level=-1):
    return filter_styles(routine["styles"], style) \
            and filter_goals(routine["goals"], goal) \
            and filter_level(routine["level"], level)

'''
[SPEC] filter_routines

INPUT:
    routines set ROUTINES :=
    [
        // Set of routine where we want to find routines satisfying a filtering option
    ]
    filtering option OPT :=
    {
        // NOTICE: All of below attributes should be given
        // Default: "Don't filter with this attribute"
        style : "Bodybuilding",         // Default = "" 
        goal  : "Build Muscle",         // Default = ""
        level : 1  (== "Intermediate")  // Default = -1
    }

OUTPUT:
    SAT_ROUTINES :=
    [
        // routines that satisfy the given filtering option
    ]
'''
def filter_routines(routines, opt):
    sat_routines = []
    
    for routine in routines:
        if filter_routine(routine, opt["style"], opt["goal"], opt["level"]):
            sat_routines.append(routine)
    return sat_routines


# ----- [END] Helper Functions for Programs/Routines Filtering -----

# ----- [START] Helper Functions for Searching Exercises -----

def search_item_by_id(items, id):
    for item in items:
        if item["_id"] == id:
            return item
    return None

# ----- [END] Helper Functions for Searching Exercises -----