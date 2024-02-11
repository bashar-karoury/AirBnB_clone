#!/usr/bin/python3
""" Unittests for place module
"""

import unittest
import sys
sys.path.insert(0, '../')  # Add the parent directory to the Python path
sys.path.insert(0, '../..')  # Add the parent directory to the Python path
from models.place import Place
from models.base_model import BaseModel
class Testing_Place(unittest.TestCase):
    """ Unit testing class for Place class
    """

    def test_init(self):
        """ test init method of Place class
        """
        s1 = Place()
        self.assertEqual(type(s1).__name__,"Place")
        check = issubclass(type(s1), BaseModel)
        self.assertEqual(True, check)

    def test_init_name(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.name, "")

    def test_init_city_id(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.city_id, "")

    def test_init_user_id(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.user_id, "")

    def test_init_description(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.description, "")

    def test_init_number_rooms(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.number_rooms, 0)

    def test_init_number_bathrooms(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.number_bathrooms, 0)

    def test_init_max_guest(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.max_guest, 0)

    def test_init_price_by_night(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.price_by_night, 0)

    def test_init_latitude(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.latitude, 0.0)

    def test_init_longitude(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.longitude, 0.0)

    def test_init_amenity_ids(self):
        """ test init method of Place is propersly assign attributes
        """
        s1 = Place()
        self.assertEqual(s1.amenity_ids, [])
