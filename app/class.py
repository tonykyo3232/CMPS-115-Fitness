# -- [START] NOT USED NOW --
class Exercise():
    pass

class Day():
    pass

class Cycle():
    pass

class Program():
    level_map = {
        "beginner": 0,
        "intermediate": 1,
        "advance": 2
    }

    def __init__(styles, goals, level, length, name, desc="", cycles=[]):
        self.styles = styles
        self.goals = goals
        self.name = name
        self.desc = desc

        # cycles: [Class Cycle]
        self.cycles = cycles

        # level: "Beginner", "BeGiNNer", "beginner" => self.level: 0
        self.level = level_map[level.lower()]
        
        # length: "32 weeks", "  32 Weeks  asdfqwef" => self.week_cnt = 32
        self.week_cnt = length

# Convert program in dictionary (general hash table) format into Class Program
def dict_to_program(prog_dict):
    pass

# -- [END] NOT USED NOW --