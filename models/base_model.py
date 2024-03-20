#!/usr/bin/python3
import uuid

"""Creating BaseModel class"""

class BaseModel:
    """This is the base model"""
    def __init__(self, id=None):
        """Initializing base class"""
        self.id = uuid.uuid4()


    def __str__(self):
        return("[{}] ({})".format(self.__class__.__name__, self.id))
