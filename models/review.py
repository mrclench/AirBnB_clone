#!/usr/bin/python3
""" Review class inheriting from basemodel class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ class names review"""
    place_id = ""
    user_id = ""
    text = ""
