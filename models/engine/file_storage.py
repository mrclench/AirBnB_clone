#!/usr/bin/python3

import json
import os


class FileStorage:
    """ This class serializes instances to Json file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all stored objects"""
        return self.__objects

    def new(self, obj):
        """ Store a new obj in objects """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Save the __objects dictionary """
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            data = {key: value.to_dict()
                    for key, value in self.__objects.items()}
            json.dump(data, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}

        return classes

    def reload(self):
        """ load the json file to the __objects dictionary """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}

                self.__objects = obj_dict
        else:
            return
