from geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, side_length, color, filled) :
        super().__init__(color, filled)
        self.__side_length = float(side_length)

    def get_side_length(self):
        return self.__side_length

    def get_area(self):
        area = 6*(self.__side_length**2)
        rounded_area = float(round(area, 2))
        return rounded_area

    def get_volume(self):
        volume = self.__side_length**3
        rounded_volue = float(round(volume, 2))
        return rounded_volue

if __name__ == '__main__':
    cube_1 = Cube(10,'red', True)
print(cube_1.get_color())
print(cube_1.get_filled())
print(cube_1.get_area())
print(cube_1.get_volume())
print(cube_1.get_side_length())
