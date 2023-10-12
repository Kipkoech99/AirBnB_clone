#!/usr/bin/python3
""" Module for the place class """

from models.base_model import BaseModel


class Place(BaseModel):
    '''
    Attributes:
        city_id: of associated city
        user_id: of associated user
        name: of the place
        description: of the place
        number_rooms: in the place
        number_bathrooms: in the place
        max_guest: max number of guests in the place
        price_by_night: for the place
        latitude: coordinates of the place
        longitude: coordinates of the place
        amenity_ids: list of amenity IDs associated with the place
    '''
    def __init__(self, *args, **kwargs):
        ''' Class constructor '''
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
