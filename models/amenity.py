#!/usr/bin/python3
"""this is a file that contains Amenity class"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ This is a Amenity class for airbnb clone inherited from BaseModel
        public attributes:
            name: str
    """
    name = ""
    def __init__(self, *args, **kwargs):
        """ initialization method
        """
        super().__init__(args, kwargs)
