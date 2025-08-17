#!/usr/bin/env python3
from exchange_rates import EXCHANGE_RATES as er

def convert(amount, from_currency, to_currency):
    if not from_currency in er or not to_currency in er:
        raise Warning()
    if not type(amount) in [int, float]:
        raise Warning('invalid amount type, it should be a number')
    if amount < 0:
        raise Warning("Negative amount values are not accepted")
    if from_currency == to_currency: #stessa valuta non ha bisogno di conversione per calcolare il cambio
        return amount
    for valuta in er:
        if valuta == from_currency:
            try:
                converted_amount = (er[from_currency][to_currency])*amount
            except KeyError:
                continue

        if valuta == to_currency:
            try:
                converted_amount = (1 / (er[to_currency][from_currency]))*amount
                
            except KeyError:
                continue
    return converted_amount
