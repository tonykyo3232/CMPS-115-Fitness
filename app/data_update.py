from parser import parse
from utils import SimpleDataManager
import os
import pickle

if not os.path.exists(SimpleDataManager.pickle_dir):
    os.makedirs(SimpleDataManager.pickle_dir)

parse("*", SimpleDataManager.programs_dir, SimpleDataManager.default_programs_pickle)
parse("*", SimpleDataManager.routines_dir, SimpleDataManager.default_routines_pickle)

with open(SimpleDataManager.custom_programs_pickle, "wb") as fp:
    pickle.dump([], fp)

with open(SimpleDataManager.custom_routines_pickle, "wb") as fp:
    pickle.dump([], fp)