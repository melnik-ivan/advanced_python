#!/usr/bin/env python3
import json
import urllib

DEFAULT_CURRENCY = 'USD'
CURRENCIES_SOURCE = 'https://api.exchangeratesapi.io/latest?base={}'.format(
    DEFAULT_CURRENCY
)
RATES = {
    'BYN': 2.08,
}

with urllib.request.urlopen(CURRENCIES_SOURCE) as response:
    for key, val in json.loads(response.readline().decode())['rates'].items():
        RATES[key] = val


def get_rate(currency_1, currency_2):
    rate_1 = RATES.get(currency_1, None)
    rate_2 = RATES.get(currency_2, None)
    if rate_1 is None or rate_2 is None:
        return None
    return rate_2 / rate_1


class Money(object):
    def __init__(self, value, currency=None):
        if not currency:
            currency = DEFAULT_CURRENCY
        self.currency = currency
        self.value = value

    def __repr__(self):
        return 'Money(value={}, currency={})'.format(repr(self.value),
                                                     repr(self.currency))

    def __str__(self):
        return '{} {}'.format(self.value, self.currency)

    def convert(self, currency):
        if self.currency == currency:
            return self.value
        rate = get_rate(self.currency, currency)
        if rate is not None:
            return self.value * rate
        raise ValueError('Invalid currency "{}"'.format(currency))

    def __add__(self, other):
        if hasattr(other, 'value') and hasattr(other, 'convert'):
            other_value = other.convert(self.currency)
            return self.__class__(self.value + other_value, self.currency)
        return self.__class__(self.value + other, self.currency)

    def __radd__(self, other):
        return self.__class__(self.value + other, self.currency)

    def __mul__(self, other):
        if hasattr(other, 'value') and hasattr(other, 'convert'):
            other_value = other.convert(self.currency)
            return self.__class__(self.value * other_value, self.currency)
        return self.__class__(self.value * other, self.currency)

    def __rmul__(self, other):
        return self.__class__(self.value * other, self.currency)
