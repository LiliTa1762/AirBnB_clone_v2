#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        the__objects = FileStorage.__objects
        if cls:
            lt = {}
            for key, value in the__objects.items():
                if value.__class__ == cls:
                    lt[key] = value
            return(lt)

        return the__objects

    def delete(self, obj=None):
        """Delete obj from __objects"""
        if obj is None:
            return

        new_obj = ("{:s}.{:s}".format(obj.__class__.__name__, obj.id))
        if new_obj in FileStorage.__objects:
            FileStorage.__objects.pop(new_obj)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """ To deserialize the JSON file to objects"""
        self.reload()
