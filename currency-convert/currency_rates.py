from api import *
from numbers import Number
import locale

# https://github.com/amrshawky/currency/blob/master/src/CurrencyConversion.php
class CurrencyRates(API):
    # all rate related class will extend this class
    __params = {
        "base": None,  # base currency
        "amount": None,  # an array of currency codes to limit output
        "symbols": None,  # amount to be converted
        "source": None,  # Switch data source (forex `default`), bank view or crypto currencies.
        "places": None,  # rounding decimal number.
    }

    __multiple = False

    results = []

    # _base_url = "https://api.exchangerate.host/convert"

    def __init__(self):
        return

    """
        Set base /from currency
        :param base
        :return self
    """
    def base(self, base):
        self.__base = base
        return self

    """
        Set target / to currency
        If multiple, set as a list
        :param target
        :return self
    """
    def target(self, target):
        self.__multiple = False
        self.__to = target

        if type(target) == list:
            self.__multiple = True

        return self

    """
        Set amount to convert
        :param amount
        :return self
    """
    def amount(self, amount: Number):
        self.__amount = amount
        return self

    """
        Set how many decimal point to show
        :param point
        :return self
    """
    def round(self, point: int):
        self.__round = point
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

    """
        Set source for bank view or cryptocurrency
        :param source
        :return self
    """
    def source(self, source):
        self.__source = source
        return self

    def _set_query_params(self, target=None):
        self._payload = {
            'from': self.__from,
            'to': self.__to if target is None else target,
            'amount': self.__amount
        }

        if self.__date:
            self._payload['date'] = self.__date  # format: YYYY-MM-DD

        if self.__source:
            self._payload['source'] = self.__source

    def get(self):
        # self.results = []
        # # for multiple target currency to convert
        # if self.__multiple:
        #     for item in self.__to:
        #         self._set_query_params(item)
        #         self.results.append(self.process(item))
        # else:
        #     self._set_query_params()
        #     self.results.append(self.process())
        #
        # results = self.results
        # self.results = []
        # return results
        return self.process()

    def process(self, target=None):
        response = super().get()
        return self._get_result(response, target)

    def _get_result(self, response, item=None):
        try:
            # result = response['result'] if response else None
            result = response.json()
            result = result['rates']
            if self.__round:
                result = round(result, self.__round)

            if self.__code:
                result = self._formatter(result)

            response = {
                "from": self.__from,
                "to": self.__to if item is None else item,
                "converted_amount": result,
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
        locale.setlocale(locale.LC_ALL, self.__code)
        currency = locale.currency(result, grouping=True)
        return currency

