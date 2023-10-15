#!/usr/bin/python3
'''Module with class Base class for the objects'''

import uuid
import datetime
import models

class BaseModel:
    '''
    Base Class for instantiation of public attributes and methods

    Attributes:
        id: UUID of the object
        created_at: timestamp when the object was created
        updated_at: time instance the object was updated

    Methods:
        __init__: class constructor
        __str__: returns string representation of the class
        save: updates the updated_at instance
        to_dict: returns dictionary representation of the object
    '''
    def __init__(self, *args, **kwargs):
        '''Class constructor'''
        if kwargs:  # initialize attributes from kwargs
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        '''Returns string repr of the object'''
        class_name = self.__class__.__name__
        return(f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        '''Updates when object was saved'''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns dictionary repr of the object'''
        instance_dict = self.__dict__.copy()  # copy of dict instance

        class_name = self.__class__.__name__  # get class name
        instance_dict['__class__'] = class_name  # add class name to the dict

        # convert to str obj (ISO formart) and add created_at to dict
        created_at_str = self.created_at.isoformat()
        instance_dict['created_at'] = created_at_str

        # convert to str object (ISO format) and add updated_at to dict
        updated_at_str = self.updated_at.isoformat()
        instance_dict['updated_at'] = updated_at_str

        return instance_dict
