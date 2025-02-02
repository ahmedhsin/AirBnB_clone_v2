#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, String, Column, Integer, Date, ForeignKey
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """ Set up an instance with its properties. """
        super().__init__(*args, **kwargs)
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """return a list of cities"""
            from models import storage
            allCities = storage.all(City)
            citie = []
            for city in allCities.values():
                if city.state_id == self.id:
                    citie.append(city)
            return citie
