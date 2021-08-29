from currency_rates import *


class CurrencyLatestRates(CurrencyRates):
    _base_url = "https://api.exchangerate.host/latest"

    def __init__(self):
        return