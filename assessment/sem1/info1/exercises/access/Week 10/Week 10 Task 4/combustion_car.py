
from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        self.__c = gas_capacity
        self.__gas_per_100km = gas_per_100km
        self.__c_max = self.__c
        if not isinstance(gas_capacity, (int, float)):
            raise Warning()
        if not isinstance(gas_per_100km, (int, float)):
            raise Warning()
        if gas_capacity < 0:
            raise Warning()
        if gas_per_100km < 0:
            raise Warning()
    def get_gas_tank_status(self):
        return (self.__c, self.__c_max)

    def get_remaining_range(self):
        return self.__c*100 /self.__gas_per_100km

    def drive(self, dist):
        if not isinstance(dist, (int, float)):
            raise Warning()
        if dist < 0:
            raise Warning()
        if dist > self.get_remaining_range():
            self.drive(self.get_remaining_range())
            raise Warning('Gas tank is depleted')
        self.__c -= (dist*self.__gas_per_100km)/100
    def fuel(self, f):
        if not isinstance(f, (int, float)):
            raise Warning()
        if f < 0:
            raise Warning()
        if self.__c + f> self.__c_max:
            raise Warning()
        self.__c += f
c = CombustionCar(40.0, 8.0)
c.drive(500)
c.get_remaining_range()
c.get_gas_tank_status()




