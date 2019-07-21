# ----- [START] Helper Functions for Programs/Routines Data management -----
import pickle
import parser
import os

class SimpleDataManager():
    pickle_dir = "./pickles/"
    default_programs_pickle = pickle_dir + "default_programs.pickle"
    default_routines_pickle = pickle_dir + "default_routines.pickle"
    custom_programs_pickle = pickle_dir + "custom_programs.pickle"
    custom_routines_pickle = pickle_dir + "custom_routines.pickle"

    workout_dir = "../Workout Dataset/"
    programs_dir = workout_dir + "programs/"
    routines_dir = workout_dir + "routines/"

    def __init__(self):
        self.programs = []
        self.load_programs()

        self.routines = []
        self.load_routines()

    def update_programs(self, delete_custom=False):
        pass

    def load_programs(self):
        self.programs = self.get_default_programs()
        custom_programs = self.get_custom_programs()

        next_id = len(self.programs)
        for custom_program in custom_programs:
            custom_program["_id"] = next_id
            next_id += 1
            self.programs.append(custom_program)
    
    def load_routines(self):
        self.routines = self.get_default_routines()
        custom_routines = self.get_custom_routines()

        next_id = len(self.routines)
        for custom_routine in custom_routines:
            custom_routine["_id"] = next_id
            next_id += 1
            self.routines.append(custom_routine)

    def get_default_programs(self):
        with open(SimpleDataManager.default_programs_pickle, "rb") as fp:
            programs = pickle.load(fp)
        return programs

    def update_default_programs(self):
        pass

    def get_custom_programs(self):
        with open(SimpleDataManager.custom_programs_pickle, "rb") as fp:
            programs = pickle.load(fp)
        return programs

    def insert_custom_program(self, program):
        # Insert to in-memory programs + Update in-disk pickle file (TODO: async, race condition management)
        
        program["is_default"] = False
        program["_id"] = len(self.programs)
        self.programs.append(program)

        if not os.path.exists(SimpleDataManager.custom_programs_pickle):
            with open(SimpleDataManager.custom_programs_pickle, "wb") as fp:
                pickle.dump([program], fp)
        else:
            with open(SimpleDataManager.custom_programs_pickle, "rb") as fp:
                custom_programs = pickle.load(fp)
            custom_programs.append(program)
            with open(SimpleDataManager.custom_programs_pickle, "wb") as fp:
                pickle.dump(custom_programs, fp)

    def get_default_routines(self):
        with open(SimpleDataManager.default_routines_pickle, "rb") as fp:
            routines = pickle.load(fp)
        return routines

    def update_default_routines(self):
        pass

    def get_custom_routines(self):
        with open(SimpleDataManager.custom_routines_pickle, "rb") as fp:
            routines = pickle.load(fp)
        return routines

    def insert_custom_routine(self, routine):
        # Insert to in-memory routines + Update in-disk pickle file (TODO: async, race condition management)
        
        routine["is_default"] = False
        routine["_id"] = len(self.routines)
        self.routines.append(routine)

        if not os.path.exists(SimpleDataManager.custom_routines_pickle):
            with open(SimpleDataManager.custom_routines_pickle, "wb") as fp:
                pickle.dump([routine], fp)
        else:
            with open(SimpleDataManager.custom_routines_pickle, "rb") as fp:
                custom_routines = pickle.load(fp)
            custom_routines.append(routine)
            with open(SimpleDataManager.custom_routines_pickle, "wb") as fp:
                pickle.dump(custom_routines, fp)

    
    # search item (program / routine) by _id
    def search_item(self, is_routine, _id):
        items = self.routines if is_routine else self.programs
        for item in items:
            if _id == item["_id"]:
                return item
        return None

# ----- [END] Helper Functions for Programs/Routines storing -----


# ----- [START] Helper Functions for Programs/Routines Filtering -----

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
