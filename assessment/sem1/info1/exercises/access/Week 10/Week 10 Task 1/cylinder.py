from geometric_object import GeometricObject


class Cylinder(GeometricObject):
    def __init__(self, radius, height,color, filled, pi = 3.14):
        super().__init__(color, filled)
        self.__height = float(height)
        self.__radius = float(radius)
        self.__pi = float(pi)

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def get_area(self):
        area = (self.__pi*(self.__radius**2)) + (2*self.__pi*self.__radius*self.__height)
        rounded_area = float(round(area, 2))
        return rounded_area

    def get_volume(self):
        volume = self.__pi*(self.__radius**2)*self.__height
        rounded_volume = float(round(volume, 2))
        return rounded_volume

if __name__ == '__main__':
    cylinder_1 = Cylinder(3.5, 6.3, "blue", True)
    cylinder_2 = Cylinder(10,5,'red',True)
print(cylinder_1.get_color())
print(cylinder_2.get_area())
print(cylinder_1.get_volume())
print(cylinder_1.get_filled())
print(cylinder_1.get_height())
print(cylinder_1.get_radius())
