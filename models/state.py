#!/usr/bin/python3
"""this is a file that contains State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ This is a state class for airbnb clone inherited from BaseModel
        public attributes:
            name: str
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialization method
        """
        super().__init__(args, kwargs)
