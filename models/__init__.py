#!/usr/bin/python3
""" This module instantiates an object of class FileStorage
"""
import sys
from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .state import State
from .city import City
from .amenity import Amenity
from .review import Review
from .place import Place
sys.path.insert(0, '../')  # Add the parent directory to the Python path
storage = FileStorage()
storage.reload()
