#!/usr/bin/python3
""" Module for city subclass unittests """

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    ''' Class for unittest methods for City '''

    def test_city(self):
        '''Test cases for city subclas'''
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
