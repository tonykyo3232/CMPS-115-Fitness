from parser import parse
from utils import SimpleDataManager
import os
import pickle
import pymongo

REMOVE_DEFAULT = 1
REMOVE_CUSTOM = 1
WORKOUT_DIR = "../Workout Dataset/"
PROGRAMS_DIR = WORKOUT_DIR + "programs/"
ROUTINES_DIR = WORKOUT_DIR + "routines/"

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
fitness_db = mongoclient["fitness"]
workouts_col = fitness_db["workouts"]



# clear entire DB if needed
if REMOVE_DEFAULT:
    workouts_col.delete_many({"is_default": False})
if REMOVE_CUSTOM:
    workouts_col.delete_many({"is_default": True})

# parse default programs and insert them into MongoDB
default_programs = parse("*", PROGRAMS_DIR)
workouts_col.insert_many(default_programs)

# parse default routines and insert them into MongoDB
default_routines = parse("*", ROUTINES_DIR)
workouts_col.insert_many(default_routines)