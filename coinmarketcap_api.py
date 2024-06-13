from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class CoinmarketcapInvalidSymbol(Exception):
  def __init__(self, symbol):
      self.symbol = symbol

  def __str__(self):
      return(repr(self.symbol))


class CoinMarketCap:

  def __init__(self, key: str, url: str, parameters: dict) -> None:
    self.API_KEY = key
    self.URL = url
    self.PARAMETERS = parameters
    self.DATA = self.call()

  def call(self) -> dict:
    session = Session()
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': self.API_KEY,
    }
    session.headers.update(headers)
    try:
      response = session.get(self.URL, params=self.PARAMETERS)
      data = json.loads(response.text)
      
      if response.status_code == 200:
        return data
      else:
        raise CoinmarketcapInvalidSymbol(data['status']['error_message'])

    except (ConnectionError, Timeout, TooManyRedirects) as e:
      raise e
      
    except CoinmarketcapInvalidSymbol as e:
      print(e)
      exit()

  def clean_coins(self):
    data = self.DATA['data']
    coins = dict()
    for coin in data.keys():
      coins[coin] = data[coin]

    return coins
