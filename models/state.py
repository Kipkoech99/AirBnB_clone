#!/usr/bin/python3
""" Module with State class """

from models.base_model import BaseModel


class State(BaseModel):
    '''
    State subclass of BaseModel class

    Methods:
        __init__: class constructor
    '''
    name = ""  # empty name -> name of the state
