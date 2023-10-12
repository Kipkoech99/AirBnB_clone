#!/usr/bin/python3
""" Module for the revie class """

from models.base_moel import BaseModel


class Review(BaseModel):
    '''
    Review subclass

    Attributes:
        place_id: of associated place
        user_id: of associated user
        text: review
    '''
    def __init__(self, *args, **kwargs):
        ''' Class constructor '''
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
