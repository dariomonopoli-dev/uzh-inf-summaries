
from shop import Shop


class Bakery(Shop):

    def __init__(self, capital):
        super().__init__(capital)
        self.__dough = 0
        self.__bread = 0

    def sell(self, price_per_unit, units):
        return super().sell(price_per_unit*0.75, units)

    def produce(self, costs_per_unit):
        if self._capital < self.__dough*costs_per_unit:
                convert_amount = self._capital //costs_per_unit
                self.__dough -= convert_amount
                self.__bread += convert_amount
                self._capital -=convert_amount*costs_per_unit
                raise Warning()
        if self._capital > self.__dough*costs_per_unit:
            self._capital -= self.__dough * costs_per_unit
            self.__bread += self.__dough
            self.__dough = 0

    def add_procured_units(self, units):
        self.__dough += units

    def set_produced_units(self, units):
        self.__bread = units

    def get_produced_units(self):
        return self.__bread

    def pay_rent_and_loan(self, rent):
        return super().pay_rent_and_loan(rent*0.8)

    def get_status(self):
        status = list(super().get_status())
        status.append(self.__dough)
        status.append(self.__bread)
        return tuple(status)