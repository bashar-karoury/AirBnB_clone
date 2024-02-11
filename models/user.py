#!/usr/bin/python3
"""this is a file that contains User class
"""
from models.base_model import BaseModel

class User(BaseModel):
    """ This is a user class for airbnb clone inherited from BaseModel
        public class attributes:
            email: str
            password: str
            first_name: str
            last_name: str
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ initialization method

            Args:
                args: tuple of arguments
                kwargs: dictionary as key with value
        """
        super().__init__(args, kwargs)
