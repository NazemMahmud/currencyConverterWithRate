from rates_latest import *
from numbers import Number
import locale


# https://github.com/amrshawky/currency/blob/master/src/CurrencyConversion.php
class Rates():
    # all currency rate type class call from here
    _base_url = "https://api.exchangerate.host/convert"

    def __init__(self):
        return

    """
        Call Latest Rate class
    """
    def latest(self):
        return CurrencyLatestRates()

