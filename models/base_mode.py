"""base_model.py
contains 1 class:
    BaseModel()
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """Defines all the common attributes/methods
    for other classes that will inherit from it"""

    def __init__(self, *args, **kwargs):
        """Initialize object"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4()) # unique id for each BaseModel
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns string format"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'updated_at' with current datetime
        invoke save() function & save to serialized file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary containing keys/values of the instance
        Basically a dictionary representation with
        “simple object type” of our BaseModel.
        Will be used in serializing/deserializing
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy


