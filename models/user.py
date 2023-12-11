#!/usr/bin/python3

"""
Title: Class <User>
Description: Write a class User that inherits from BaseModel
Authors: Elizabeth Akindele & Idoko Attah
"""

from models.base_model import BaseModel

class User(BaseModel):
    """ User class definition """
    
    first_name = ""
    last_name = ""
    email = ""
    password = ""
