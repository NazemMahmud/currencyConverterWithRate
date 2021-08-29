from converter import *
from rates import *


# https://github.com/amrshawky/currency/blob/master/src/Currency.php
class Currency:
    def __init__(self):
        return

    @staticmethod
    def convert():
        return CurrencyConverter()

    @staticmethod
    def rates():
        return Rates()

# url = 'https://api.exchangerate.host/convert?from=USD&to=EUR&amount=1'
# response = requests.get(url)
# data = response.json()
