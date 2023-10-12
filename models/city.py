#!/usr/bin/python3
'''Module for city subclass'''

from models.base_model import BaseModel
from datetime import datetime


class City(BaseModel):
    ''' City class for storing city information

    Attributes:
        state_id: ID of associated state
        name: name of the city
    '''
    def __init__(self, *args, **kwargs):
        '''class constructor'''
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
