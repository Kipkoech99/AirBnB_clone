#!/usr/bin/python3
""" Module for the revie class """

from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Review subclass

    Attributes:
        place_id: of associated place
        user_id: of associated user
        text: review
    '''
        place_id = ""
        user_id = ""
        text = ""
