from parser import parse
from utils import SimpleDataManager
import os
import pickle
import pymongo

REMOVE_DEFAULT = 1
REMOVE_CUSTOM = 1

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
fitness_db = mongoclient["fitness"]
workouts_col = fitness_db["workouts"]

if not os.path.exists(SimpleDataManager.pickle_dir):
    os.makedirs(SimpleDataManager.pickle_dir)


# clear entire DB if needed
if REMOVE_DEFAULT:
    workouts_col.delete_many({"is_default": False})
if REMOVE_CUSTOM:
    workouts_col.delete_many({"is_default": True})

# parse default programs and insert them into MongoDB
default_programs = parse("*", SimpleDataManager.programs_dir, SimpleDataManager.default_programs_pickle)
workouts_col.insert_many(default_programs)

# parse default routines and insert them into MongoDB
default_routines = parse("*", SimpleDataManager.routines_dir, SimpleDataManager.default_routines_pickle)
workouts_col.insert_many(default_routines)

with open(SimpleDataManager.custom_programs_pickle, "wb") as fp:
    pickle.dump([], fp)

with open(SimpleDataManager.custom_routines_pickle, "wb") as fp:
    pickle.dump([], fp)