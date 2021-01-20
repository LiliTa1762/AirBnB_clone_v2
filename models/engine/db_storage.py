#!/usr/bin/python3
"""New engine for hbnb clone"""


import json
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os
from sqlalchemy.orm import scoped_session
""" from models.amenity import Amenity """
""" from models.place import Place """
""" from models.review import Review """
""" from models.user import User """

# Get environment variables
HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')


class DBStorage:
    """ This class manage the new engine """

    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of new engine """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB
            ),
            pool_pre_ping=True
        )

    def all(self, cls=None):
        """Returns the dict of objects of one type of class

        Args:
            cls (obj, optional): an object to filter the query.
            Defaults to None.
        """
        session = self.__session
        if cls:
            rs = session.query(cls).all()
            querys_list = [rs]
        else:
            st = session.query(State).all()
            ct = session.query(City).all()
            us = session.query(User).all()
            """rw = session.query(Review).all()
            pl = session.query(Place).all()
            am = session.query(Amenity).all() """

            querys_list = [st, ct, us]
            """ for i in querys:
                if type(i) is list: """

        dic = {}
        for rs in querys_list:
            for obj in rs:
                k = '{}.{}'.format(obj.__class__.__name__, obj.id)
                if '_sa_instance_state' in obj.__dict__:
                    obj.__dict__.pop('_sa_instance_state')
                dic[k] = obj
        return(dic)

    def new(self, obj):
        """ Add obj"""
        self.__session.add(obj)

    def save(self):
        """ Save obj"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reload obj """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """ To close session """
        self.__session.close()
