#!/usr/bin/python3
""" This module instantiates an object of class FileStorage
"""
import sys
from models.engine.file_storage import FileStorage
sys.path.insert(0, '../')  # Add the parent directory to the Python path
storage = FileStorage()
storage.reload()
