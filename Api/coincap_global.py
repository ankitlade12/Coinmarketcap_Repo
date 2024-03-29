import json
from datetime import datetime
import requests

currency = 'INR'

global_url = 'https://api.coinmarketcap.com/v2/global/?convert=' +currency

request = requests.get(global_url)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = results['data']['quotes'][currency]['total_market_cap']
global_volume = results['data']['quotes'][currency]['total_volume_24h']

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)

last_update_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

print()
print('There are currently ' +active_currencies_string+ ' active currencies and ' +active_markets_string)
print('The global cap of all cryptos is ' +global_cap_string+ ' and the 24th global volume is ' +global_volume_string)
print()
print('Bitcoin\'s total percentage of the global cap is ' +str(bitcoin_percentage) +'%')
print()
print('This information was last updated on ' +str(last_update_string) )