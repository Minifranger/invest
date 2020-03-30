import os
import json
import logging
import boto3
from trade.alphavantage.alphavantage import ALPHAVANTAGE_TS
from utils import validate_params, failure

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def intraday(event, context):
    logger.info('event : {event}'.format(event=event))
    path, = validate_params(path=event.get('pathParameters'))

    symbol = path.get('symbol')
    if not symbol:
        return failure(code=400, body='You should provide a symbol to your path parameters')

    logger.info('Getting stock intraday {symbol}'.format(symbol=symbol))

    try:
        result = ALPHAVANTAGE_TS.get_intraday(**event.get('pathParameters'))
        print(result)
        # if not result.get('Item'):
        #     return success(status_code=204, body=json.dumps(result.get('Item'), cls=DecimalEncoder))
    except Exception as e:
        return failure(body=e)
    #
    # logger.info('Retrieved item {id}'.format(id=id))
    # return success(body=json.dumps(result.get('Item'), cls=DecimalEncoder))
