import requests
import json
from config import keys
class ConvertionException(Exception):
    pass
class MoneyConvertor :
    @staticmethod
    def convert(first:str,second:str,cash:str):
        if first==second:
           raise ConvertionException(f'Невозможно перевести одинаковые валюты {first}.')
        try: first_ticker=keys[first.lower()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {first}')
        try: second_tiker=keys[second.lower()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {second}')
        try: cash=float(cash)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {cash}')
        if cash<0:raise ConvertionException(f'Введено отрицательное число {cash}')
        r=requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={first_ticker}&tsyms={second_tiker}')
        total_base=json.loads(r.content)[keys[second]]
        return total_base
