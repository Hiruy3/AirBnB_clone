#!/usr/bin/python3
"""
Class City that inherit from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City info"""
    state_id = ''
    name = ''
