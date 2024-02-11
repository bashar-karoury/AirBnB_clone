#!/usr/bin/python3
"""this is a file that contains Place class"""
from models.base_model import BaseModel

class Place(BaseModel):
    """ This is a Place class for airbnb clone inherited from BaseModel
        public attributes:
            city_id: (str)
            user_id: (str)
            name: (str)
            description: (str)
            number_rooms: (int)
            number_bathrooms: (int)
            max_guest: (int)
            price_by_night: (int)
            latitude: (float)
            longitude: (float)
            amenity_ids: (list[strings])
    """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ initialization method
        """
        super().__init__(args, kwargs)

