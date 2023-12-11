"""
file_storage.py
contains 1 class:
    File_Storage()
"""

import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}

    def __init__(self):
        pass

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """stores in __objects an obj
        with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serialize __objects to JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            d = { k : v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes JSON file to __objects if file exists"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                obj_dict = json.load(f)
            for value in obj_dict.values():
                self.new(self.class_dict[value["__class__"]](**value))
        except FileNotFoundError:
            pass
