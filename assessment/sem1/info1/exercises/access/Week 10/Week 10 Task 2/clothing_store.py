#!/usr/bin/env python3

from shop import Shop


class ClothingStore(Shop):

    def __init__(self, capital):
        super().__init__(capital)
        self.__clothing_pieces = 0

    def procure(self, price_per_unit, units):
        if units > 10:
            return super().procure(0.8*price_per_unit, units)
        return super().procure(price_per_unit*1.0, units)
    
    def add_procured_units(self, units):
        self.__clothing_pieces += units

    def get_produced_units(self):
        return self.__clothing_pieces

    def set_produced_units(self, units):
        self.__clothing_pieces = units

    def get_status(self):
        status = list(super().get_status())
        status.append(self.__clothing_pieces)
        return tuple(status)