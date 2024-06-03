#!/usr/bin/python3
""" A class names city that inherits from Basemodel """

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city"""
    state_id = ""
    name = ""
