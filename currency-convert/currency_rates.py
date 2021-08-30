from api import *
from numbers import Number
import locale

# https://github.com/amrshawky/currency/blob/master/src/CurrencyConversion.php
class CurrencyRates(API):
    # all rate related class will extend this class
    __params = dict.fromkeys(["base", "amount", "symbols", "source", "places"])
    # __params = {
    #     "base": None,  # base currency
    #     "amount": None,  # an array of currency codes to limit output
    #     "symbols": None,  # amount to be converted
    #     "source": None,  # Switch data source (forex `default`), bank view or crypto currencies.
    #     "places": None,  # rounding decimal number.
    # }

    __code = None
    results = []

    # _base_url = "https://api.exchangerate.host/convert"

    def __init__(self):
        return

    """
        Set base /from currency
        :param base : string type 3 letter code, like, BDT, EUR, USD, etc.
            default EUR (euro)
        :return self
        optional
    """
    def base(self, base: str):
        self.__params["base"] = base
        return self

    """
        Set target currencies
        :param target: string type
            If multiple, then comma separated, like EUR,BDT,CZK
        :return self
    """
    def target(self, target: str):
        self.__params["symbols"] = target
        return self

    """
        Set amount to convert
        :param amount
        :return self
    """
    def amount(self, amount: Number):
        self.__params["amount"] = amount
        return self

    """
        Set how many decimal point to show
        :param point
        :return self
    """
    def places(self, point: int):
        self.__params["places"] = point
        return self

    """
        Set source for bank view or crypto-currency
        :param source
        :return self
    """
    def source(self, source):
        self.__params["source"] = source
        return self

    """
        Set local currency format language code
        :param code
        :return self
    """
    def format(self, code: str):
        self.__code = code
        return self

    """
        Set date for historical exchange currency
        :param date
        :return self
    """
    def date(self, date):
        self.__date = date
        return self

    def _set_query_params(self):
        for key, value in self.__params.items():
            if value:
                self._payload[key] = value

        # if self.__date:
        #     self._payload['date'] = self.__date  # format: YYYY-MM-DD

    def get(self):
        self._set_query_params()
        response = super().get()
        return self._get_result(response)

    def _get_result(self, response):
        try:
            result = response.json()
            rates = result['rates']

            if self.__code:
                rates = self._formatter(result)

            response = {
                "rates": rates,
                'success': True
            }
            return response
        except:
            response = {
                'success': False,
                "message": "Something went wrong in the server, please wait"
            }
            return response

    def _formatter(self, result):
        rates = result['rates']
        locale.setlocale(locale.LC_ALL, self.__code)
        if 'timeseries' in result.keys() and result['timeseries']:
            return self.time_series_formatter(rates)
        elif 'fluctuation' in result.keys() and result['fluctuation']:
            return self.fluctuation_formatter(rates)
        else:
            for key, value in rates.items():
                rates[key] = locale.currency(value, grouping=True)
            return rates

    def time_series_formatter(self, result):
        for item in result:
            obj = result[item]
            for code, amount in obj.items():
                obj[code] = locale.currency(amount, grouping=True)
            result[item] = obj
        return result

    def fluctuation_formatter(self, result):
        for item in result:
            obj = result[item]
            for key, value in obj.items():
                if key == 'start_rate' or key == 'end_rate':
                    obj[key] = locale.currency(value, grouping=True)
            result[item] = obj
        return result
