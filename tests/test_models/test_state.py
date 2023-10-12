#!/usr/bin/python3
""" Unittest module for state class """

import unittest
from models.state import State


class TestState(unittest.TestCase):
    ''' test for class state '''
    def test_state(self):
        ''' Test cases for state subclass '''
        state = State()
        self.assertEqual(state.name, "")
