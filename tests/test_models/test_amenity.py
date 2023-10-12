#!/usr/bin/python3
""" Module for class Amenity test cases """

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    ''' class for Amenity unittest methods '''

    def test_amenity(self):
        '''Test cases for amenity subclass'''
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
