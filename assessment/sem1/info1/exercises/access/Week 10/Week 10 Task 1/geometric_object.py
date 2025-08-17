from abc import ABC, abstractmethod



class GeometricObject (ABC):
    def __init__(self, color, filled):
        self.__color = color
        self.__filled = filled

    def set_color(self, color):
        self.__color = color

    def set_filled(self, filled):
        self.__filled = filled

    def get_color(self):
        return self.__color

    def get_filled(self):
        return self.__filled

    @abstractmethod
    def get_area(self):
        return self.__rounded_area

    @abstractmethod
    def get_volume(self):
        return self.__rounded_volume



    

    

