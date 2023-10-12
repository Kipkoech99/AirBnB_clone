#!/usr/bin/python3
""" Module with State class """

from models.base_model import BaseModel
from datetime import datetime


class State(BaseModel):
    '''
    State subclass of BaseModel class

    Methods:
        __init__: class constructor
    '''
    def __init__(self, *args, **kwargs):
        ''' state class constructor '''
        super().__init__(*args, **kwargs)  # call constructor of parent class
        self.name = ""  # empty name -> name of the state
