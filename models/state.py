#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String() nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
