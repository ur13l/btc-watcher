import json
import bitso


def handler(event, context):

    api = bitso.Api()
    tick = api.ticker("btc_mxn")

    body = {"message": "BTCMXN", "ticker": str(tick.last)}

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
