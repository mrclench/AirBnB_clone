![AirBnB Clone Logo](https://www.aydentownsley.com/img/hbnb.png)

# AirBnB Clone Project

Welcome to the AirBnB clone project! This is the first step towards building your first full web application: the AirBnB clone. This initial step is crucial as it forms the foundation for all subsequent projects including HTML/CSS templating, database storage, API, and front-end integration.

## Table of Contents
- [Background Context](#background-context)
- [What’s a Command Interpreter?](#whats-a-command-interpreter)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
  - [Python Scripts](#python-scripts)
  - [Python Unit Tests](#python-unit-tests)

## Background Context
The first step involves writing a command interpreter to manage AirBnB objects. This interpreter will:
- Establish a parent class (BaseModel) to handle initialization, serialization, and deserialization of instances.
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Develop all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- Implement the first abstracted storage engine: File storage.
- Write unittests to validate all classes and the storage engine.

## What’s a Command Interpreter?
Similar to the Shell but limited to our specific use-case, the command interpreter will manage the objects of our project:
- Create new objects (e.g., a new User or a new Place)
- Retrieve objects from a file, database, etc.
- Perform operations on objects (count, compute stats, etc.)
- Update attributes of objects
- Destroy objects

## Resources
Read or watch:
- [cmd module](https://docs.python.org/3/library/cmd.html)
- [cmd module in depth](https://pymotw.com/3/cmd/)
- [Packages concept page](https://docs.python.org/3/tutorial/modules.html#packages)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [args/kwargs](https://realpython.com/python-kwargs-and-args/)
- [Python test cheatsheet](https://docs.python-guide.org/writing/tests/)
- [cmd module wiki page](https://en.wikipedia.org/wiki/Cmd_(Python_module))
- [python unittest](https://docs.python.org/3/library/unittest.html)

## Learning Objectives
By the end of this project, you should be able to explain:
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is a UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Code should use the `pycodestyle` (version 2.8.*)
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should be a real sentence explaining the purpose of the module, class, or method.

### Python Unit Tests
- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- All test files should be inside a folder `tests`
- Use the `unittest` module
- All test files should be Python files (extension: `.py`)
- All test files and folders should start by `test_`
- File organization in the `tests` folder should mirror the project structure
  - For `models/base_model.py`, unit tests should be in: `tests/test_models/test_base_model.py`
  - For `models/user.py`, unit tests should be in: `tests/test_models/test_user.py`
- All tests should be executed using: `python3 -m unittest discover tests`
- You can also test file by file using: `python3 -m unittest tests/test_models/test_base_model.py`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Collaborate on test cases to ensure no edge cases are missed.

## How to Use the Program

### Starting the Command Interpreter
To start the command interpreter, run the following command in your terminal:

./console.py
### Basic Commands

The command interpreter supports the following commands:

- create <class_name>: Creates a new instance of the specified class and prints its ID.
-   show <class_name> <id>: Prints the string representation of an instance based on the class name and ID.
-   destroy <class_name> <id>: Deletes an instance based on the class name and ID.
-   all [<class_name>]: Prints all string representations of instances optionally filtered by class name.
-   update <class_name> <id> <attribute_name> <attribute_value>: Updates an instance based on the class name and ID by adding or updating an attribute.

 

## Contributing
Contributions to this project are welcome. Please follow the guidelines outlined in this document and ensure all code is well-documented and tested.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
