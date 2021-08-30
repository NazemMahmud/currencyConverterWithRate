from currency_rates import *


class Rates(CurrencyRates):
    # all currency rate type class call from here

    def __init__(self):
        return

    """
        Call for Latest Rate
    """
    def latest(self):
        self._base_url = "https://api.exchangerate.host/latest"
        return self

    """
        Call for historical rate
        :param date: date must be in YYYY-MM-DD format
        required param
        Historical rates are available for most currencies all the way back to the year of 1999.
    """
    def historical(self, date):
        self._base_url = "https://api.exchangerate.host/" + date
        return self

    """
        Call for timeseries rate
        :param start_date: date must be in YYYY-MM-DD format
        :param end_date: date must be in YYYY-MM-DD format
        both are required params
        Timeseries are for daily historical rates between two dates of your choice, 
        with a maximum time frame of 365 days. 
        This will return an array or null on failure.
    """
    def timeseries(self, start_date, end_date):
        self._base_url = "https://api.exchangerate.host/timeseries"
        self._payload["start_date"] = start_date
        self._payload["end_date"] = end_date
        return self

    """
        Call for timeseries rate
        :param start_date: date must be in YYYY-MM-DD format
        :param end_date: date must be in YYYY-MM-DD format
        both are required params
        Retrieve information about how currencies fluctuate on a day-to-day basis, 
        with a maximum time frame of 365 days. 
        This will return an array or null on failure.
    """
    def fluctuations(self, start_date, end_date):
        self._base_url = "https://api.exchangerate.host/fluctuation"
        self._payload["start_date"] = start_date
        self._payload["end_date"] = end_date
        return self
