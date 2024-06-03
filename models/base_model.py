#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This is a base model class for our program.
    defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor method for BaseModel.
        Initializes a new instance of BaseModel with the given name.
        """
        if kwargs is not None and kwargs:
            for arg in kwargs:
                if arg == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif arg == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif arg != "__class__":
                    self.__dict__[arg] = kwargs[arg]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()  # Assign current datetime
            self.updated_at = datetime.now()  # Assign current datetime
            storage.new(self)

    def __str__(self):
        """Returns a string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates time by saving new current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns data in the dictionary"""
        obj_dict = self.__dict__.copy()
        """Arrange the tuple and process the data that is in JSON"""
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
