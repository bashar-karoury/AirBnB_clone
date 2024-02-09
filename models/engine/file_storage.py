#!/usr/bin/python3

"""this is a file that contains storage class"""
import json

class FileStorage():
    """Class for saving data in a json file"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns objects"""
        return self.__objects

    def new(self, obj):
        """sets a new object in __objects"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as File:
            json_dict = dict()
            for key, value in (self.__objects).items():
                json_dict[key] = value.to_dict()
            json.dump(json_dict, File, default=str)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from ..base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file:
                json_dict = json.load(file)
                temp_objs = {}
                for key, value in json_dict.items():
                    temp_objs[key] = BaseModel(**value)
                self.__objects = temp_objs
        except Exception as e:
            print(e)
