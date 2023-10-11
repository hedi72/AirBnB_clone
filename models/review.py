#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review inherits from BaseModel
        Args:
            place_id: string - empty string: it will be the Place.id
            user_id: string - empty string: it will be the User.id
            text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
