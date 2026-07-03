import pickle
from abc import ABC, abstractmethod

class AbstractDAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__object_cache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
    
    def __dump(self):
        with open(self.__datasource, "wb") as f:
            pickle.dump(self.__object_cache, f)
    
    def __load(self):
        with open(self.__datasource, "rb") as f:
            self.__object_cache = pickle.load(f)
    
    def add(self, key, obj):
        self.__object_cache[key] = obj
        self.__dump()
    
    def get(self, key):
        try:
            return self.__object_cache[key]
        except KeyError:
            return None
    
    def remove(self, key):
        try:
            del self.__object_cache[key]
            self.__dump()
        except KeyError:
            pass
    
    def get_all(self):
        return list(self.__object_cache.values())