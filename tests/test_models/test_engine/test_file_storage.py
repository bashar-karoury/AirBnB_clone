#!/usr/bin/python3
""" Unittests for file_storage module
"""

import unittest
import sys
import json
sys.path.insert(0, '../')  # Add the parent directory to the Python path
sys.path.insert(0, '../..')  # Add the parent directory to the Python path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
class Testing_FileStorage(unittest.TestCase):
    """ Unit testing class for FileStorage class
    """

    def test_all(self):
        """ test all method of FileStorage class
        """
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_new(self):
        """ test new method of FileStoarge
        """
        b1 = BaseModel()
        fs = FileStorage()
        fs.new(b1)
        check = b1 in fs.all().values()
        self.assertEqual(True, check)

    def test_save(self):
        """ test save method of FileStorage class
        """
        fs = FileStorage()
        dict_1 = fs.all()
        b1 = BaseModel()
        fs.new(b1)
        fs.save()
        fs.reload()
        # shouldn't be the same
        self.assertNotEqual(dict_1, fs.all())

    def test_reload(self):
        """ test reload method of FileStorage
        """
        # set objects in file
        fs = FileStorage()
        dict_1 = fs.all()
        b1 = BaseModel()
        fs.new(b1)
        fs.save()
        fs.reload()
        # shouldn't be the same
        self.assertNotEqual(dict_1, fs.all())

