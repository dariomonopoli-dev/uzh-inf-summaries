#!/usr/bin/env python3
from currency_converter import convert
from exchange_rates import EXCHANGE_RATES as er

class BankAccount:

    def __init__(self, currency="CHF"):
        if currency not in er:
            raise Warning('Unkown currency')
        self.__currency = currency
        self.__balance = 0

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount, currency="CHF"):
        self.__amount = amount
        if not currency in er:
            raise Warning("The bank can't recognize the entered currency")
        if not type(amount) in [int, float]:
            raise Warning('invalid amount type')
        if amount < 0:
            raise Warning('invalid amount value, it should be positive')
        try:
             convert(amount, currency, self.__currency)
        except Warning:
            return 'Unable to convert due to an Error'
        self.__balance+=convert(amount, currency, self.__currency)

        
    def withdraw(self, amount, currency="CHF"):
        if not currency in er:
            raise Warning("The bank can't recognize the entered currency")
        if not type(amount) in [int, float]:
            raise Warning('invalid amount type')
        if amount < 0:
            raise Warning('invalid amount value, it should be positive')
        try:
             convert(amount, currency, self.__currency)
        except Warning:
            return 'Unable to convert due to an Error'
        if self.get_balance() < convert(amount, currency, self.__currency):
            raise Warning('fondi insufficienti per withdraware')
        self.__balance-=convert(amount, currency, self.__currency)

        
sut = BankAccount("CHF")
sut.deposit(100.0, "CHF")
sut.withdraw(10.0, "EUR")
print(sut.get_balance())