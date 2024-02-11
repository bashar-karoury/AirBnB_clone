#!/usr/bin/python3
""" Unittests for review module
"""

import unittest
import sys
sys.path.insert(0, '../')  # Add the parent directory to the Python path
sys.path.insert(0, '../..')  # Add the parent directory to the Python path
from models.review import Review
from models.base_model import BaseModel
class Testing_Review(unittest.TestCase):
    """ Unit testing class for Review class
    """

    def test_init(self):
        """ test init method of Review class
        """
        s1 = Review()
        self.assertEqual(type(s1).__name__,"Review")
        check = issubclass(type(s1), BaseModel)
        self.assertEqual(True, check)

    def test_init_place_id(self):
        """ test init method of Review is propersly assign attributes
        """
        s1 = Review()
        self.assertEqual(s1.place_id, "")

    def test_init_user_id(self):
        """ test init method of Review is propersly assign attributes
        """
        s1 = Review()
        self.assertEqual(s1.user_id, "")

    def test_init_text(self):
        """ test init method of Review is propersly assign attributes
        """
        s1 = Review()
        self.assertEqual(s1.text, "")
