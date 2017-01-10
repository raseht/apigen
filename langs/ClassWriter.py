from abc import ABC, abstractmethod

class ClassWriter(ABC):
    @abstractmethod
    def open_class(name,access):
        pass
    
    @abstractmethod
    def add_member(name,type,value,access):
        pass
    
    @abstractmethod
    def close_class():
        pass
    