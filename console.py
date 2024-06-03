#!/usr/bin/python3
"""This module is for constrolling the console"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json
from shlex import split


def parse(args):
    """split a string into a list"""
    list = split(args)
    return list


def extract_info(string):
    """
    Regular expression pattern to match
    the class, method, and arguments
    """

    pattern = r'(\w+)\.(\w+)\((.*?)\)'

    match = re.match(pattern, string)

    if match:
        class_name = match.group(1)
        method_name = match.group(2)
        arguments_str = match.group(3).strip()
        if arguments_str:
            arguments_list = re.split(r',\s*(?=[^\}]*(?:\{|$))', arguments_str)
            arguments = [arg.strip().strip('"').strip("'")
                         for arg in arguments_list]
        else:
            arguments = []
        return class_name, method_name, arguments
    else:
        return None


class HBNBCommand(cmd.Cmd):
    """
    Class to intercept the console cmd
    and execute our code
    """
    prompt = '(hbnb) '
    __classes = {"BaseModel", "User",
                 "City", "Place", "State",
                 "Review", "Amenity"}

    def default(self, line):
        class_name, method_name, arguments = extract_info(line)
        if len(arguments) == 0:
            self.onecmd("{} {}".format(method_name, class_name))
        else:
            if method_name == "update":
                if len(arguments) == 3:
                    self.onecmd("{} {} {} {} {}".format(method_name,
                                                        class_name,
                                                        arguments[0],
                                                        arguments[1],
                                                        arguments[2]))
                elif len(arguments) == 2:
                    try:
                        tmp = arguments[1].replace('\'', '"').replace("\\", "")
                        print(tmp)
                        potential_dict = json.loads(tmp)
                        if isinstance(potential_dict, dict):
                            print("is dict instance")
                            for k, v in potential_dict.items():
                                self.onecmd("{} {} {} {} {}".format(
                                    method_name,
                                    class_name,
                                    arguments[0],
                                    k,
                                    v
                                ))
                    except json.JSONDecodeError:
                        self.onecmd("{} {} {} {}".format(method_name,
                                                         class_name,
                                                         arguments[0],
                                                         arguments[1]))
                elif len(arguments) == 1:
                    self.onecmd("{} {} {}".format(method_name,
                                                  class_name, arguments[0]))

            else:
                self.onecmd("{} {} {}".format(method_name,
                                              class_name, arguments[0]))

    def do_quit(self, line):
        "Quits console"
        return True

    def do_EOF(self, line):
        "Exits console"
        return True

    def emptyline(self):
        """Do nothing"""
        pass

    def do_create(self, line):
        """
        Create a new instance of a class.
        Usage: create <class_name>
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line in self.__classes:
            classes = storage.classes()
            obj = classes[line]()
            print(obj.id)
            obj.save()
        else:
            print("** class doesn't exist **")

    def do_count(self, line):
        """
        Print the count of the objects stored in JSON file
        Usage: count <class_name> or <class>.count()
        """
        args = parse(line)
        objects = storage.all()

        if len(args) == 1 and args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            list_objects = []
            for obj in objects.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    list_objects.append(obj.__str__())
                elif len(args) == 0:
                    list_objects.append(obj.__str__())
            print(len(list_objects))

    def do_show(self, line):
        """
        Shows an instance of a class using the
        class name and id
        Usage: show <class_name> <id> or
        <class_name>.show(<id>)
        """

        args = parse(line)

        objects = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" in objects:
            print(objects[f"{args[0]}.{args[1]}"])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Destroy a class instance using
        the class name and id
        Usage: destroy <class_name> <id> or
        <class_name>.destroy(<id>)
        """
        args = parse(line)
        objects = storage.all()

        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" in objects:
            del objects[f"{args[0]}.{args[1]}"]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints a list of strings of all
        class instances
        Usage: all <class_name> or all
        """
        args = parse(line)
        objects = storage.all()

        if len(args) == 1 and args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            list_objects = []
            for obj in objects.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    list_objects.append(obj.__str__())
                elif len(args) == 0:
                    list_objects.append(obj.__str__())
            print(list_objects)

    def do_update(self, line):
        """
        update a class instance using
        the class name and id
        Usage: update <class_name> <id> <attribute>
        <value> or <class_name>.update(<id>, attriute,
        value)
        """
        args = parse(line)
        objects = storage.all()

        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")

        if len(args) == 4:
            if f"{args[0]}.{args[1]}" in objects:
                attribute = args[2]
                value = args[3]
                obj = objects["{}.{}".format(args[0], args[1])]
                if attribute in obj.to_dict().keys():
                    cast = type(getattr(obj, attribute))
                    setattr(obj, attribute, cast(value))
                else:
                    setattr(obj, attribute, value)

                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
