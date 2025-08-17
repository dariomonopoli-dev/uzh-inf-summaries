from abc import ABC, abstractmethod
class Animal(ABC):
    pass
class Cat(Animal):
    def __init__(self):
        pass
class Shiam(Cat):
    def __init__(self,name):
        self.name = name
        super().__init__(name) #--> eredita super dalla classe Cat, non dalla classe Animal
