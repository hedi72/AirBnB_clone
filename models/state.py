#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    """ class State inherits from Model
        Args:
            name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
