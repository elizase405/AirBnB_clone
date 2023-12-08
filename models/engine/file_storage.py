"""
file_storage.py
contains 1 class:
    File_Storage()
"""

import json
import os.path

class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """stores in __objects an the obj
        with key <obj class name>.id"""
        key = f"{self.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serialize __objects to JSON file"""
        json.dump(self.__objects, self.__file_path)

    def reload(self):
        """deserializes JSON file to __objects if file exists"""
        if os.path.isfile(self.__file_path) == False:
            pass
        else:
            json.load(self.__file_path)

