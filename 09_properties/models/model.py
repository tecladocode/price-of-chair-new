from abc import ABCMeta, abstractmethod

from common.database import Database


class Model(metaclass=ABCMeta):
    @property
    def collection(self):
        return self._collection
    
    @collection.setter
    def collection(self, value):
        self._collection = value
    
    @property
    def _id(self):
        return self.__id
    
    @_id.setter
    def _id(self, value):
        self.__id = value
        
    def save_to_mongo(self):
        Database.update(self.collection, {"_id": self._id}, self.json())
    
    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})
    
    @classmethod
    def get_by_id(cls, _id: str):
        return cls(**Database.find_one(cls.collection, {"_id": _id}))
    
    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find(cls.collection, {})]
    
    @classmethod
    def find_one_by(cls, attribute, value):
        return cls(**Database.find_one(cls.collection, {attribute: value}))
    
    @classmethod
    def find_many_by(cls, attribute, value):
        return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
    
    @abstractmethod
    def json(self):
        raise NotImplementedError