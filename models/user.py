#!/usr/bin/python3
"""A class user that inherent from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        User class intherits from BaseModel
        Args:
            email: string - empty string
            password: string - empty string
            first_name: string - empty string
            last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
