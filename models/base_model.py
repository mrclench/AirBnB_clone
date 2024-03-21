#!/usr/bin/python3
import uuid
from datetime import datetime

"""Creating BaseModel class"""


class BaseModel:
    """This is the base model"""
    def __init__(self):
        """Initializing base class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = ""
        self.my_number = 0

    def __str__(self):
        """Returns a human-readable, string representation of an object"""
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
