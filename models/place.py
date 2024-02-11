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
    def __init__(self, *args, **kwargs):
        """ initialization method
        """
        super().__init__(args, kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

