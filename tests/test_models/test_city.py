#!/usr/bin/python3
""" Unittests for city module
"""

import unittest
import sys
sys.path.insert(0, '../')  # Add the parent directory to the Python path
sys.path.insert(0, '../..')  # Add the parent directory to the Python path
from models.city import City
from models.base_model import BaseModel
class Testing_City(unittest.TestCase):
    """ Unit testing class for City class
    """

    def test_init(self):
        """ test init method of City class
        """
        s1 = City()
        self.assertEqual(type(s1).__name__,"City")
        check = issubclass(type(s1), BaseModel)
        self.assertEqual(True, check)

    def test_init_name(self):
        """ test init method of City is propersly assign attributes
        """
        s1 = City()
        self.assertEqual(s1.name, "")

    def test_init_state_id(self):
        """ test init method of City is propersly assign attributes
        """
        s1 = City()
        self.assertEqual(s1.state_id, "")
