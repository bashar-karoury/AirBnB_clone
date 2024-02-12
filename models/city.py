#!/usr/bin/python3
"""this is a file that contains City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ This is a city class for airbnb clone inherited from BaseModel
        public attributes:
            state_id: str
            name: str
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialization method
        """
        super().__init__(args, kwargs)
