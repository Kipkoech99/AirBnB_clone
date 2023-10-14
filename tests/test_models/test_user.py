#!/usr/bin/python3
""" Module with unittests for class User """

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    ''' class with all unittest methods '''

    def test_attributes(self):
        ''' test user attributes during user creation '''
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inherited_attributes(self):
        ''' ensures user attributes are inherited correctly '''
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))

    def test_attributes_assignment(self):
        ''' ensures user attributes are assigned correctly '''
        user = User()
        user.email = "example@example.com"
        user.password = "example_password"
        user.first_name = "Eljones"
        user.last_name = "Doe"
        self.assertEqual(user.email, "example@example.com")
        self.assertEqual(user.password, "example_password")
        self.assertEqual(user.first_name, "Eljones")
        self.assertEqual(user.last_name, "Doe")
