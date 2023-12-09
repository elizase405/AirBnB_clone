#!/usr/bin/python3
"""
file_storage.py
contains 1 class:
    File_Storage()
"""

import json
import os.path
from models.user import User
from models.base_model import BaseModel


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
        # json.dump(self.__objects, self.__file_path)
        obj_dict = {}
        for obj in self.__objects.keys():
            obj_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes JSON file to __objects if file exists"""
        if os.path.isfile(self.__file_path) == False:
            pass
        else:
            # Open the file in read mode and use json.load
            with open(self.__file_path, 'r') as file:
                try:
                    obj_dict = json.load(file)
                    for classId, val in obj_dict.items():
                        Class, ID = classId.split('.')
                        val["created_at"] = datetime.fromisoformat(val["created_at"])
                        val["updated_at"] = datetime.fromisoformat(val["updated_at"])
                        inst = eval(Class)(**val)
                        self.__objects[classId] = inst
                except Exception:
                    pass
