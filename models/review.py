#!/usr/bin/python3
"""this is a file that contains Review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """ This is a Review class for airbnb clone inherited from BaseModel
        public attributes:
            place_id: str
            user_id: str
            text: str
    """
    def __init__(self, *args, **kwargs):
        """ initialization method
        """
        super().__init__(args, kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
