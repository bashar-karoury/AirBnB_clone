#!/usr/bin/python3
"""this is a file that contains User class"""
from models import storage
from models.base_model import BaseModel

class User(BaseModel):
    """ This is a user class for airbnb clone inherited from BaseModel
        public attributes:
            email: str
            password: str
            first_name: str
            last_name: str
    """
    def __init__(self, *args, **kwargs):
        """ initialization method
        """
        super().__init__(args, kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
