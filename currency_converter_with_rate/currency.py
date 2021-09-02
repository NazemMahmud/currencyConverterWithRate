from .converter import *
from .rates import *

class Currency:
    def __init__(self):
        return

    @staticmethod
    def convert():
        return CurrencyConverter()

    @staticmethod
    def rates():
        return Rates()
