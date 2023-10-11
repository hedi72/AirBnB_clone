#!/usr/bin/python3
"""
This is the base model for which other classes inherit public
instance attributes and methods
"""


import uuid
from datetime import datetime
import models


class BaseModel():
    """
    Base Model with all common methods and attributes

    Class_methods:
        __init__: Instantiation of attributes
        save: Updates the public instance attribute with the current time
        to_dict: Returns a dictionary with all keys of __dict__
        __str__: base class attributes in string format
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation of attributes.

        args:
            *args: This is the variable length of the list of arguments
            **kwargs: This allows to pass any number of keyword arguments

        If kwargs != empty:
            * each key corresponds to an attribute name
            * each value in the kwargs dictionary is used as a value
            * Specifically, if the attribute name is 'created_at' or
                'updated_at', their values are converted to datetime objects
        Else:
            * id is generated using uuid.uuid4()
            * created_at attribute os set to the current datetime
            * updated_at is also set to the current datetime,
                matching created_at
        """
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Representation of base class attributes in string format."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updated_at is updated with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Dictionary is returned containing all keys of __dict__ of the instance.
        """
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)
