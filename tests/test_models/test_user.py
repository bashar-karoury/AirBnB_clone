#!/usr/bin/python3
""" Unittests for user module
"""

import unittest
import sys
sys.path.insert(0, '../')  # Add the parent directory to the Python path
sys.path.insert(0, '../..')  # Add the parent directory to the Python path
from models.user import User
from models.base_model import BaseModel
class Testing_BaseModel(unittest.TestCase):
    """ Unit testing class for User class
    """

    def test_init(self):
        """ test init method of User class
        """
        u1 = User()
        self.assertEqual(type(b1).__name__,"User")
        check = issubclass(BaseModel, u1)
        self.assertEqual(True, check)

    def test_init_email(self):
        """ test init method of User is propersly assign attributes
        """
        u1 = User()
        self.assertEqual(u1.email, "")

    def test_init_password(self):
        """ test init method of User is propersly assign attributes
        """
        u1 = User()
        self.assertEqual(u1.password, "")

    def test_init_first_name(self):
        """ test init method of User is propersly assign attributes
        """
        u1 = User()
        self.assertEqual(u1.first_name, "")

    def test_init_last_name(self):
        """ test init method of User is propersly assign attributes
        """
        u1 = User()
        self.assertEqual(u1.last_name, "")


