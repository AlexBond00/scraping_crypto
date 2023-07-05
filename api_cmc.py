from pprint import pprint

import requests
from requests import Request, Session
import json

def getInfo(coin):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    api = 'eeea1287-dbda-47da-86ec-ca580fe74b3b'
    parameters = {'slug': f'{coin}',
                  'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api
    }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    pprint(response.json())
    with open('text.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

    return response.json()


id_coin = {
    'bitcoin': 1,
    'ethereum': 1027,
    'tether': 825,
    'bnb': 1839,
    'usd-coin': 3408,
    'xrp': 52,
    'cardano': 2010,
    'dogecoin': 74,
    'litecoin': 2,
    'solana': 5426,
    'tron': 1958,
    'polygon': 3890,
    'polkadot-new': 6636,
    'bitcoin-cash': 1831,
    'toncoin': 11419,
    'wrapped-bitcoin': 3717,
    'multi-collateral-dai': 4943,
    'avalanche': 5805,
    'shiba-inu': 5994,
    'binance-usd': 4687
}

