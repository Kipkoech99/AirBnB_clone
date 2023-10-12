#!/usr/bin/python3
"""
    This module creates a class that is used in serialization \
            and deserialization of JSON files
"""
import json
import os

class FileStorage:
    """serialization/deserialization class"""

    __file_path = 'file.json'
    __objects = {}
    __classes = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)
        """
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            for k, v in obj_dict.items():
                class_name = v.get("__class__", None)
                if class_name and class_name in self.__classes:
                    self.__objects[k] = self.__classes[class_name](**v)

    @classmethod
    def classes(cls):
        """Returns dictionary of available classes"""
        return cls.__classes
