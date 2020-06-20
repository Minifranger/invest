import os

import boto3
from alpha_vantage.timeseries import TimeSeries


class Alphavantage(TimeSeries):
    _zone = 'PAR'

    def __init__(self):
        self.key = boto3.client('ssm').get_parameter(Name=os.environ['ALPHAVANTAGE_SECRET'], WithDecryption=True).get(
            'Parameter').get('Value')
        super().__init__(key=self.key)
