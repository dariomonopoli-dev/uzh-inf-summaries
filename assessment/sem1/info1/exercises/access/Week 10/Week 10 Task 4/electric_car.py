
from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        self.__e_max = battery_size
        self.__battery_range_km = battery_range_km
        self.__e = battery_size
        if not isinstance (self.__e_max, (int, float)):
            raise Warning()
        if not isinstance (self.__battery_range_km, (int, float)):
            raise Warning()
        if self.__e_max < 0:
            raise Warning()
        if self.__battery_range_km < 0:
            raise Warning()


    def get_battery_status(self):
        return (self.__e, self.__e_max)

    def get_remaining_range(self):
        return self.__battery_range_km*self.__e/self.__e_max

    def drive(self, dist):
        if not isinstance(dist, (int, float)):
            raise Warning()
        if dist < 0:
            raise Warning()
        if dist > self.get_remaining_range():
            self.drive(self.get_remaining_range())
            raise Warning('Battery tank is depleted')
        self.__e -= (dist*5)/100


    def charge(self, kwh):
        if not isinstance(kwh, (int, float)):
            raise Warning()
        if kwh < 0:
            raise Warning()
        if self.__e +kwh> self.__e_max:
            raise Warning()
        self.__e+=kwh

