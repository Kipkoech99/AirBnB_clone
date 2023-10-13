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
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
