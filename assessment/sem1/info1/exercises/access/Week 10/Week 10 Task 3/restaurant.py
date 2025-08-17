#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.
import copy


class Restaurant:

    def __init__(self, name, cuisine_type, is_open = False):
        self._name = str(name)
        self.__cuisine_type = str(cuisine_type)
        self.__is_open = is_open
        self.__menu = dict()
        self.__sale_amount = 0

    def describe_restaurant(self):
        return f'{self._name}, {self.__cuisine_type}'

    def open_restaurant(self):
        self.__is_open = True

    def close_restaurant(self):
        self.__is_open = False

    def is_open(self):
        return self.__is_open

    def add_consumption_unit(self, name, price):
            self.__menu[name] = price

    def remove_consumption_unit(self, name):
        del self.__menu[name]

    def get_menu(self):
        return copy.deepcopy(self.__menu)


    def sell_unit(self, name):
        if not self.__is_open:
            raise Warning()
        self.__sale_amount += self.__menu[name]

    def get_sales(self):
        return self.__sale_amount


r = Restaurant("Random Restaurant", "Mixed Cuisine")
r.add_consumption_unit("Caesar Salad", 15)
print(r.is_open())
r.open_restaurant()
r.sell_unit("Caesar Salad")
r.sell_unit("Caesar Salad")
print(r.get_sales())




