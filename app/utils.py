# ----- [START] Helper Functions for Filtering -----

def filter_styles(prog_styles, style_opt):
    if style_opt == "":
        return True

    for style in prog_styles:
        if style_opt.lower() in style.lower():
            return True
    return False

def filter_goals(prog_goals, goal_opt):
    if goal_opt == "":
        return True

    for goal in prog_goals:
        if goal_opt.lower() in goal.lower():
            return True
    return False

# prog_level, level: 1  (meaning "intermediate")
def filter_level(prog_level, level):
    if level == -1:
        # Do not filter by level if level == -1 (default)
        return True
    return prog_level == level


# Note: PROG_LEN := string expression of program length "4 Weeks"
def filter_length(prog_len, len_min, len_max):
    # Convert prog_len into number of weeks ("4 weeks" => 4)
    # Assumption: prog_len looks like "    1234    weeks asdfqwer"
    length_token = prog_len.lower().split("week")[0].strip()
    if not length_token.isnumeric():
        raise Exception("Wrong length format")

    length = int(length_token)
    if len_min != -1 and len_min > length:
        return False
    if len_max != -1 and len_max < length:
        return False
    return True


def filter_program(prog, style="", goal="", level=-1, len_min=-1, len_max=-1): 
    return filter_styles(prog["styles"], style) \
            and filter_goals(prog["goals"], goal) \
            and filter_level(prog["level"], level) \
            and filter_length(prog["length"], len_min, len_max)

test_program = {
    "name": "My Beginner Program",
    "styles": ["General Fitness"],
    "level": 0,
    "length": "6 Weeks",
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
    program set PROGS :=
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
    SAT_PROGS :=
    [
        // Programs that satisfy the given filtering option
    ]
'''
def filter_programs(progs, opt):
    sat_progs = []
    
    for prog in progs:
        if filter_program(prog, opt["style"], opt["goal"],
                opt["level"], opt["len_min"], opt["len_max"]):
            sat_progs.append(prog)
    return sat_progs

assert [test_program] == filter_programs([test_program], test_opt)
        


def filter_routine(rout, style="", goal="", level=-1):
    return filter_styles(rout["styles"], style) \
            and filter_goals(rout["goals"], goal) \
            and filter_level(rout["level"], level)

'''
[SPEC] filter_routines

INPUT:
    routines set routs :=
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
    SAT_ROUTS :=
    [
        // routines that satisfy the given filtering option
    ]
'''
def filter_routines(routs, opt):
    sat_routs = []
    
    for rout in routs:
        if filter_routine(rout, opt["style"], opt["goal"], opt["level"]):
            sat_routs.append(rout)
    return sat_routs


# ----- [END] Helper Functions for Filtering -----
