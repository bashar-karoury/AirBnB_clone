#!/usr/bin/python3
""" Unittests for base_model module
"""

import unittest
import sys
sys.path.insert(0, '../')  # Add the parent directory to the Python path
sys.path.insert(0, '../..')  # Add the parent directory to the Python path
from models.base_model import BaseModel
class Testing_BaseModel(unittest.TestCase):
    """ Unit testing class for BaseModel class
    """

    def test_init(self):
        """ test init method of BaseModel class
        """
        b1 = BaseModel()
        self.assertEqual(type(b1).__name__,"BaseModel")

    def test_init_created_updated(self):
        """ test init method of BaseModel class creates created_at time
        """
        b1 = BaseModel()
        import datetime
        c1 = b1.created_at.isoformat()
        c2 = b1.updated_at.isoformat()
        self.assertEqual(c1[:-3], c2[:-3])

    def test_init_id(self):
        """ test init method of BaseModel class creates unique id
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id , b2.id)

    def test_str(self):
        """ test str method of BaseModel class
        """
        b1 = BaseModel()
        s1 = str(b1)
        s2 = "[BaseModel] ({}) {}".format(b1.id, b1.__dict__)
        self.assertEqual(s1, s2)

    def test_save(self):
        """ test save method of BaseModel class creates created_at time
        """
        b1 = BaseModel()
        import datetime
        b1.save()
        c1 = b1.created_at.isoformat()
        c2 = b1.updated_at.isoformat()
        self.assertGreater(c2, c1)


    def test_to_dict(self):
        """ test to_dict method of BaseModel class
        """
        b1 = BaseModel()
        dict_ = b1.__dict__.copy()
        dict_["__class__"] = b1.__class__.__name__
        dict_["created_at"] = b1.created_at.isoformat()
        dict_["updated_at"] = b1.updated_at.isoformat()

        self.assertEqual(b1.to_dict(), dict_)

