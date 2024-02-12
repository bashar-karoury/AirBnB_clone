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
    place_id = ""
    user_id = ""
    text = ""
