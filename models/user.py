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

    def __str__(self):
        """String representaion of User

            Returns: string representation of object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
