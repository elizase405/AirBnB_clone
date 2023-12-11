#!/usr/bin/python3

"""place.py
Contains 1 class:
    Place()
"""

from base_model import BaseModel

class Place(BaseModel):
    """inherits from basemodel
    Args:
        BaseModel
    """

    city_id = "" #City.id
    user_id = "" #User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [] #list of Amenity.id

    def __init__(self):
        pass
