import requests
from abc import ABC, abstractmethod


class API(ABC):
    _base_url = None
    _payload = {}

    """
        To set query parameters
    """
    @abstractmethod
    def _set_query_params(self):
        pass

    """
        To get result in a format
    """
    @abstractmethod
    def _get_result(self):
        pass

    """
        To local language formatter
    """
    @abstractmethod
    def _formatter(self):
        pass

    def get(self):
        response = requests.get(self._base_url, params=self._payload)
        return response


