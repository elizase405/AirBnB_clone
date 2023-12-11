#!/usr/bin/python3

"""review.py
Contains 1 class:
    Review()
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """inherits from basemodel
    Args:
        BaseModel
    """

    place_id = "" #Place.id
    user_id = "" #User,id
    text = ""

    def __init__(self):
        pass
