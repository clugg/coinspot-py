# coinspot-py

A Python 2 and 3 compatible SDK for the [CoinSpot](https://www.coinspot.com.au/) API.

# Prerequisites

* Python 2.7+ or Python 3.0+
* [python-requests](python-requests.org)

A compatible version of `python-requests` can be installed via `$ pip install -r requirements.txt`.

# Usage

```python
>>> from coinspot import CoinSpot
>>> cs = CoinSpot("YOUR_API_KEY", "YOUR_API_SECRET")
>>> cs.latest()
{'status': 'ok', 'prices': {'btc': {'bid': '20200', 'ask': '20649.98', 'last': '20649.98'}, 'ltc': {'bid': '347', 'ask': '362.48', 'last': '347'}, 'doge': {'bid': '0.01721', 'ask': '0.018', 'last': '0.01799'}}}
>>> cs.my_balances()
{'status': 'ok', 'balance': {'aud': 0, 'btc': 0, 'ltc': 0, 'doge': 0, 'ppc': 0, 'wdc': 0, 'xpm': 0, 'max': 0, 'lot': 0, 'qrk': 0, 'moon': 0, 'ftc': 0, 'drk': 0}}
>>> cs.my_coin_deposit('BTC')
{'status': 'ok', 'address': '1JVyVgKg9yNiPatm7c1g3hD4yjZ72xjUpD'}```

All available functionality is listed at [CoinSpot's API reference](https://www.coinspot.com.au/api). Any available URL listed is accessible through this SDK by replacing slashes with underscores. For example, the URL `/my/coin/deposit` is accessible via a CoinSpot instance's `my_coin_deposit` method.
