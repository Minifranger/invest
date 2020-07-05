import os

import boto3
from alpha_vantage.timeseries import TimeSeries


class Alphavantage(TimeSeries):
    __list_index__ = ['airbus', 'engie']
    __region__ = 'Paris'

    def __init__(self, **kwargs):
        if not kwargs.get('key'):
            kwargs.update({'key': boto3.client('ssm').get_parameter(Name=os.environ['ALPHAVANTAGE_SECRET'],
                                                                    WithDecryption=True).get('Parameter').get('Value')})
        self.__region__ = kwargs.get('__region__', self.__region__)
        super().__init__(**kwargs)

    def get_intraday(self, **kwargs):
        result = super().get_intraday(**kwargs)
        result = self._adjust_timezone()
        return result

    def get_symbol_search(self, **kwargs):
        result, _ = super().get_symbol_search(**kwargs)
        result = self._filter_region(l=result, **kwargs)
        return result

    def _filter_region(self, **kwargs):
        return list(filter(lambda x: x.get('4. region') == self.__region__, kwargs.get('l', [])))

    def _adjust_timezone(self):
        return
