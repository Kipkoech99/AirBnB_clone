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
        for k, v in self.__objects.items():
            d[key] = obj.to_dict()
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                    for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
