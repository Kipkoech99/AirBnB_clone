#!/usr/bin/python3
'''Module for city subclass'''

from models.base_model import BaseModel


class City(BaseModel):
    ''' City class for storing city information

    Attributes:
        state_id: ID of associated state
        name: name of the city
    '''
    state_id = ""
    name = ""
