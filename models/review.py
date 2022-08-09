#!/usr/bin/python3
"""
Class Review that inherit from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review of the place"""
    place_id = ''
    user_id = ''
    text = ''
