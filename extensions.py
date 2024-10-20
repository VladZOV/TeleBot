import requests
import json
from config import keys


class ConvertExceptions(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote, base, amount):

        if quote == base:
            raise ConvertExceptions(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertExceptions(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertExceptions(f'Не удалось обработать валюту {base}')

        try:
            amount = int(amount)
        except ValueError:
            raise ConvertExceptions(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
