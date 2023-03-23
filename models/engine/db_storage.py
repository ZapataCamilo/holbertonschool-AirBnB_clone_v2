#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """ This class manage al database storage for HnB"""
    __engine = None
    __session = None

    def _init_(self):
        ''' Init method for dbstorage'''
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_password')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, database), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        ''' Returns all cls in DB'''
        ret_dict = {}
        if cls:
            for obj in self.__session.query(cls):
                k = '{}.{}'.format(type(obj)._name_, obj.id)
                ret_dict[k] = obj
        else:
            class_list = [State, City, User, Place, Amenity, Review]
            for cls in class_list:
                for obj in self.__session.query(cls):
                    k = '{}.{}'.format(type(obj)._name_, obj.id)
                    ret_dict[k] = obj
        return ret_dict

    def new(self, obj):
        ''' Add obj to session '''
        self.__session.add(obj)

    def save(self):
        ''' Commit new previous additions '''
        self.__session.commit()

    def delete(self, obj=None):
        ''' Deletes obj if exists '''
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        ''' Creates all tables from DB '''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
