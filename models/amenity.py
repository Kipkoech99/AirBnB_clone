#!/usr/bin/python3
""" Module for the amenity class """

from models.base_model import BaseModel
from datetime import datetime


class Amenity(BaseModel):
    '''
    Class for storing amenity information

    Attributes:
        name: of the amenity
    '''
    def __init__(self, *args, **kwargs):
        ''' Class constructor '''
        super().__init__(*args, **kwargs)
        self.name = ""
