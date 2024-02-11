#!/usr/bin/python3
""" Unittests for state module
"""

import unittest
import sys
sys.path.insert(0, '../')  # Add the parent directory to the Python path
sys.path.insert(0, '../..')  # Add the parent directory to the Python path
from models.state import State
from models.base_model import BaseModel
class Testing_State(unittest.TestCase):
    """ Unit testing class for State class
    """

    def test_init(self):
        """ test init method of State class
        """
        s1 = State()
        self.assertEqual(type(s1).__name__,"State")
        check = issubclass(type(s1), BaseModel)
        self.assertEqual(True, check)

    def test_init_name(self):
        """ test init method of State is propersly assign attributes
        """
        s1 = State()
        self.assertEqual(s1.name, "")
