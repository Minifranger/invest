import os
from alpha_vantage.timeseries import TimeSeries


class Alphavantage(TimeSeries):
    _zone = 'PAR'

    def __init__(self):
        super().__init__(key=os.environ['ALPHAVANTAGE_SECRET'])
