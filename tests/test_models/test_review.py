#!/usr/bin/python3
""" Module for Review class unittests """

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    ''' Class for Review test methods '''

    def test_review(self):
        ''' Test cases for review subclass '''
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
