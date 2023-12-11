#!/usr/bin/python3

"""city.py
Contains 1 class:
    City()
"""

from models.base_model import BaseModel

class City(BaseModel):
    """inherits from basemodel
    Args:
        BaseModel
    """

    state_id = "" #State.id
    name = ""

    def __init__(self):
        pass
