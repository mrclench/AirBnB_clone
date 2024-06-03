#!/usr/bin/python3
"""Creating class user that inherits from BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
