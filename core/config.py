import json
from pathlib import Path

import discord

BASE_DIR = Path(__file__).parent.parent.absolute()

# store needed data in a dictionnary-like object you can easyly access and edit
# you can either use defined methods or access it like a dictionnary
class data_manager:
    data = {}
    def __init__(self) -> None:
        # trigger data loading
        self.load()

    # load data from disk
    def load(self):
        # read data from the json file and parse it to dictionnary
        self.data = json.load(open(BASE_DIR / "data" / "datas.json", "r"))

    # save data to disk
    def save(self):
        # parse dictionnary to json string and write it into a file
        open(BASE_DIR / "data" / "datas.json", "w").write(self.__str__())

    # access a value
    def get(self, key) -> any:
        # get value from dictionnary, return None if doesn't exit
        return self.data.get(key)
    
    # add value
    def edit(self, key, value):
        # write value to dict
        self.data[key] = value
        self.save()

    def __str__(self) -> str:
        return json.dumps(self.data, indent=4)
    
    # allow to access data like a dictionnary
    def __getitem__(self, key):
        return self.data[key]
    
    # allow to edit data like a dictionnary
    def __setitem__(self, key, value):
        self.data[key] = value
        # update data on disk
        self.save()

# create a data_manager instance
MNGR = data_manager()