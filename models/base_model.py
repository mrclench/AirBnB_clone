#!/usr/bin/python3
import uuid
from datetime import datetime

"""Creating BaseModel class"""

class BaseModel:
    """This is the base model"""
    def __init__(self):
        """Initializing base class"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = ""
        self.my_number = 0

    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

