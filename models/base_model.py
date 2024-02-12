#!/usr/bin/python3
""" this is a file that contains BaseModel class as the base of all other
    classes.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """This is a base class for airbnb clone
    public attributes:
            id: string
            created_at: datetime of today
            updated_at: datetime of today
    """

    def __init__(self, *args, **kwargs):
        """init method for our class

            Args:
                args: tuple of arguments
                kwargs: key value list as dictionary
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        """updates the public instance attribute updated_at
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of instance

            Returns: dictionary of obj for serialization
        """
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = self.created_at.isoformat()
        dict_["updated_at"] = self.updated_at.isoformat()
        return dict_

    def __str__(self):
        """String representaion of BaseModel

            Returns: string representation of object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
