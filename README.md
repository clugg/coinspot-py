#AUTHOR Derek Chan
#GitHub https://github.com/NET-OF-BEING

A Python 2 and 3 compatible SDK for the [CoinSpot](https://www.coinspot.com.au/) API.

## Prerequisites

* Python 2.7+ or Python 3.0+
* [python-requests](https://requests.kennethreitz.org/)

A compatible version of `python-requests` can be installed via `$ pip install -r requirements.txt`.



REMEMBER to assign your API key and secret to the _api_key and _api_secret variables, as they are currently blank.
paste your API key and secret in config.py!

## Usage

```python
>>> from coinspot import CoinSpot
>>> cs = CoinSpot("YOUR_API_KEY", "YOUR_API_SECRET")
>>> cs.latest()
{'status': 'ok', 'prices': {'btc': {'bid': '20200', 'ask': '20649.98', 'last': '20649.98'}, 'ltc': {'bid': '347', 'ask': '362.48', 'last': '347'}, 'doge': {'bid': '0.01721', 'ask': '0.018', 'last': '0.01799'}}}
>>> cs.my_balances()
{'status': 'ok', 'balance': {'aud': 0, 'btc': 0, 'ltc': 0, 'doge': 0, 'ppc': 0, 'wdc': 0, 'xpm': 0, 'max': 0, 'lot': 0, 'qrk': 0, 'moon': 0, 'ftc': 0, 'drk': 0}}
>>> cs.my_coin_deposit('BTC')
{'status': 'ok', 'address': '1JVyVgKg9yNiPatm7c1g3hD4yjZ72xjUpD'}
```

All available functionality is listed at [CoinSpot's API reference](https://www.coinspot.com.au/api). Any available URL listed is accessible through this SDK by replacing slashes with underscores. For example, the URL '/my/coin/deposit' is accessible via a CoinSpot instance's `my_coin_deposit` method.


Please feel free to DONATE!  
------------------------------------------------------ 
Bitcoin : 16K2LKdXXt4GXKyZYvu8Q9qrWYQGaEtyNa
LiteCoin : ML8HdH13wEwRcBMh7VHgLb8LNMYBsBdn8T
DRGN : 0x7b4be22a721763fc6d64ccb431aa588195162544
XRP : 632217416
ETH : 0x7b4be22a721763fc6d64ccb431aa588195162544
LINK : 0x7b4be22a721763fc6d64ccb431aa588195162544
-----------------------------------------------------

