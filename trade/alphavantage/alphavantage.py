import os
from alpha_vantage.timeseries import TimeSeries


def alphavantage_ts():
    return TimeSeries(key=os.environ('ALPHAVANTAGE_SECRET'))


ALPHAVANTAGE_TS = alphavantage_ts()
