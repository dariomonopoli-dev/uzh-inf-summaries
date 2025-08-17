
from geometric_object import GeometricObject


class Cone(GeometricObject):
    def __init__(self, radius, vertical_height, slant_height,color, filled, pi = 3.14):
        super().__init__(str(color), bool(filled))
        self.__vertical_height = float(vertical_height)
        self.__slant_height = float(slant_height)
        self.__radius = float(radius)
        self.__pi = float(pi)

    def get_radius(self):
        return self.__radius

    def get_vertical_height(self):
        return self.__vertical_height

    def get_slant_height(self):
        return self.__slant_height
   
    def get_area(self):
        area = (self.__pi*(self.__radius**2))+(self.__pi*self.__radius*self.__slant_height)
        rounded_area = float(round(area, 2))
        return rounded_area

    def get_volume(self):
        volume = 1/3*(self.__pi*(self.__radius**2)*self.__vertical_height)
        rounded_volume = float(round(volume, 2))
        return rounded_volume


        
if __name__ == '__main__':
    cone_1 = Cone(10, 5, 6.4, "yellow", False)
    print(cone_1.get_area())
    print(cone_1.get_volume())
    print(cone_1.get_color())
    print(cone_1.get_filled())
    print(cone_1.get_vertical_height())
    print(cone_1.get_slant_height())
    