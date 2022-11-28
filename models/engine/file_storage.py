#!/usr/bin/python3


import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FilesStorage:
    """
    FileStorage class for serialization and deserialazing object into and from 
    files
    """
    __file__path = 'file.json'
    __objects = dict()

    def __init__(self):
        """
        init method for FileStorage class
        """
        pass

    def all(self):
        """ returns the dictionary_objects
        """
        return FilesStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>. id

        Attributes:
            obj (python object): The object to set
        """
        dictionary = obj.to_dict()
        key = '{}.{}'.format(dictionary['__class__'], str(obj.id))
        FilesStorage.__objects[key] = obj

    def save(self):
        """serilizes _objects to the JSON file (path: __file__path)
        """
        dictionary = dict()
        for k, v in FilesStorage.__objects.items():
            dictionary[k] = v.to_dict()
        with open(FilesStorage.__file__path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

    def reload(self):
        """deserializes the JSON file to __objects ONLY if the JSON file do
        exist, else do nothing. But if file do not exist, an exception should
        be raised
        """
        try:
            with open(FilesStorage.__file__path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for k, v in json_load.items():
                FilesStorage.__objects[k] = BaseModel(**v)
        except:
            pass
