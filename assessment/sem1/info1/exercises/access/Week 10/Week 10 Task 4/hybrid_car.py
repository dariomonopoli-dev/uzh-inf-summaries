#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__mode = 'car mode'

    def switch_to_combustion(self):
        self.__mode = 'Combustion'
        
    def switch_to_electric(self):
        self.__mode = 'Electric'

    def get_remaining_range(self):
            return CombustionCar.get_remaining_range(self) + ElectricCar.get_remaining_range(self)

    def drive(self, dist):
        if not isinstance(dist, (int, float)):
            raise Warning
        if dist < 0:
            raise Warning()
        Combustion_range = CombustionCar.get_remaining_range(self)
        Electric_range = ElectricCar.get_remaining_range(self)
        if dist > self.get_remaining_range():
            CombustionCar.drive(Combustion_range)
            ElectricCar.drive(Electric_range)
            raise Warning('both modes depleted')
        if self.__mode == 'Combustion':
            if Combustion_range <= dist:
                CombustionCar.drive(self, Combustion_range)
                self.switch_to_electric()
                ElectricCar.drive(self, dist - Combustion_range)
            else: CombustionCar.drive(self, dist)
        elif self.__mode == 'Electric':
            if Electric_range <= dist:
                ElectricCar.drive(self, Electric_range)
                self.switch_to_combustion()
                CombustionCar.drive(self, dist - Electric_range)
            else: ElectricCar.drive(self, dist)
h = HybridCar(40.0, 8.0, 25.0, 500.0)
h.get_battery_status()
h.switch_to_combustion()
h.drive(600.0) # depletes fuel, auto-switch
h.get_gas_tank_status() # (0.0, 40.0)
h.get_battery_status() # (20.0, 25.0)
