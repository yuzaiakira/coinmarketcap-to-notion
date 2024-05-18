from notion import Client
from coinmarketcap_api import CoinMarketCap
import os
from dotenv import load_dotenv



if __name__ == '__main__':
    load_dotenv()
    
    client = Client(token=os.getenv('I_TOKEN'), database_id=os.getenv('DATABASE_ID'))
    client.migrate_database()
    
    parameters = {
        'symbol': ','.join(client.get_symbols())
    }
    
    api = CoinMarketCap(key=os.getenv('COINMARKETCAP_KEY'), url='https://pro-api.coinmarketcap.com/v2/cryptocurrency/info', parameters=parameters)
    client.get_pages_data(api.clean_coins())
    