#!/usr/bin/python3
""" Unittests for amenity module
"""

import unittest
import sys
sys.path.insert(0, '../')  # Add the parent directory to the Python path
sys.path.insert(0, '../..')  # Add the parent directory to the Python path
from models.amenity import Amenity
from models.base_model import BaseModel
class Testing_Amenity(unittest.TestCase):
    """ Unit testing class for Amenity class
    """

    def test_init(self):
        """ test init method of Amenity class
        """
        s1 = Amenity()
        self.assertEqual(type(s1).__name__,"Amenity")
        check = issubclass(type(s1), BaseModel)
        self.assertEqual(True, check)

    def test_init_name(self):
        """ test init method of Amenity is propersly assign attributes
        """
        s1 = Amenity()
        self.assertEqual(s1.name, "")
