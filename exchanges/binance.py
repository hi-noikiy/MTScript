import os

from .base import BaseExchange


class BinanceExchange(BaseExchange):
    def __init__(self):
        super().__init__()
        self.exchange = 'binance'
        self.exchange_id = 338
        self.base_url = 'https://www.binance.com/exchange'

        self.ticker_url = '/public/product'

        self.alias = '币安'
        self.with_name = False
        self.exchange_conf = os.path.abspath(os.path.dirname(__file__)) +\
            '/exchange_conf/{}.json'.format(self.exchange)

    def get_remote_data(self):
        url = '{}{}'.format(
            self.base_url, self.ticker_url)
        return self.ticker_callback(self.get_json_request(url))

    def ticker_callback(self, result):
        return_data = []

        for i in result['data']:
            symbol = i['baseAsset']
            anchor = i['quoteAsset']
            pair = '{}/{}'.format(symbol.upper(), anchor.upper())

            return_data.append({
                'pair': pair,
                'price': i['close'],
                'volume_anchor': float(i['volume']) * i['prevClose'],
                'volume': float(i['volume']),
            })

        # print(return_data)
        return return_data
