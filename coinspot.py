import hashlib
import hmac
import json
from time import time
from hashlib import sha512

import requests


class CoinSpot(object):
    # The endpoint for the API
    API_ENDPOINT = "https://www.coinspot.com.au:443/api/"

    """Sets up the user's API key and secret.

    Args:
        key: Your API key generated from the settings page.
        sign: The POST data is to be signed using your secret key
              according to HMAC-SHA512 method.
    """
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret.encode()

    """Yields the input, resulting in Transfer-Encoding: chunked while
    using the requests library.

    Args:
        data: Data to make generator for.

    Returns:
        A generator containing the data provided.
    """
    def _chunker(self, data):
        yield data

    """Forms a request to the private API using the path and data provided,
    automatically including a nonce and signature for the data.

    Args:
        path: API endpoint to interact with.
        data (optional): Data to send with request.

    Returns:
        A Response instance.
    """
    def _request(self, path, data=None):
        if data is None:
            data = {}

        data["nonce"] = int(time() * 1000)
        json_data = json.dumps(data, separators=(',', ':')).encode()

        return requests.post(
            self.API_ENDPOINT + path,
            data=self._chunker(json_data),
            headers={
                "Content-Type": "application/json",
                "sign": hmac.new(self.secret, json_data, sha512).hexdigest(),
                "key": self.key,
            }
        ).json()

    """Latest Prices

    Returns:
        status: ok, error
        prices: object containing one property for each coin
                with the latest prices for that coin
    """
    @staticmethod
    def latest():
        return requests.get("https://www.coinspot.com.au/pubapi/latest").json()

    """List Open Orders

    Args:
        cointype: the coin shortname, example value 'BTC', 'LTC', 'DOGE'

    Returns:
        status: ok, error
        buyorders: array containing all the open buy orders
        sellorders: array containing all the open sell orders
    """
    def orders(self, cointype):
        return self._request("orders", {
            "cointype": cointype
        })

    """List Order History

    Args:
        cointype: the coin shortname, example value 'BTC', 'LTC', 'DOGE'

    Returns:
        status: ok, error
        orders: list of the last 1000 completed orders
    """
    def orders_history(self, cointype):
        return self._request("orders/history", {
            "cointype": cointype
        })

    """List My Balances

    Returns:
        status: ok, error
        balances: object containing one property for each coin
                  with your balance for that coin.
    """
    def my_balances(self):
        return self._request("my/balances")

    """List My Orders
    A list of your open orders by coin type, it will
    return a maximum of 100 results

    Returns:
        status: ok, error
        buyorders: array containing all your buy orders
        sellorders: array containing all your sell orders
    """
    def my_orders(self):
        return self._request("my/orders")

    """Place Buy Order

    Args:
        cointype: the coin shortname, example value 'BTC', 'LTC', 'DOGE'
        amount: the amount of coins you want to buy,
                max precision 8 decimal places
        rate: the rate in AUD you are willing to pay,
              max precision 6 decimal places

    Returns:
        status: ok, error
    """
    def my_buy(self, cointype, amount, rate):
        return self._request("my/buy", {
            "cointype": cointype,
            "amount": amount,
            "rate": rate
        })

    """Cancel Buy Order

    Args:
        id: the id of the order to cancel

    Returns:
        status: ok, error
    """
    def my_buy_cancel(self, _id):
        return self._request("my/buy/cancel", {
            "id": _id
        })

    """Place Sell Order

    Args:
        cointype: the coin shortname, example value 'BTC', 'LTC', 'DOGE'
        amount: the amount of coins you want to sell,
                max precision 8 decimal places
        rate: the rate in AUD you are willing to sell for,
              max precision 6 decimal places

    Returns:
        status: ok, error
    """
    def my_sell(self, cointype, amount, rate):
        return self._request("my/sell", {
            "cointype": cointype,
            "amount": amount,
            "rate": rate
        })

    """Cancel Sell Order

    Args:
        id: the id of the order to cancel

    Returns:
        status: ok, error
    """
    def my_sell_cancel(self, _id):
        return self._request("my/sell/cancel", {
            "id": _id
        })

    """Deposit Coins

    Args:
        cointype: the coin shortname, example value 'BTC', 'LTC', 'DOGE'

    Returns:
        status: ok, error
        address: your deposit address for the coin
    """
    def my_coin_deposit(self, cointype):
        return self._request("my/coin/deposit", {
            "cointype": cointype
        })

    """Quick Buy Quote

    Args:
        cointype: the coin shortname, example value 'BTC', 'LTC', 'DOGE'
        amount: the amount of coins to buy

    Returns:
        status: ok, error
        quote: the rate per coin
        timeframe: estimate hours to wait for trade to complete
                   (0 = immediate trade)
    """
    def quote_buy(self, cointype, amount):
        return self._request("quote/buy", {
            "cointype": cointype,
            "amount": amount
        })

    """Quick Sell Quote

    Args:
        cointype: the coin shortname, example value 'BTC', 'LTC', 'DOGE'
        amount: the amount of coins to sell

    Returns:
        status: ok, error
        quote: the rate per coin
        timeframe: estimate hours to wait for trade to complete
                   (0 = immediate trade)
    """
    def quote_sell(self, cointype, amount):
        return self._request("quote/sell", {
            "cointype": cointype,
            "amount": amount
        })


    """Display Coin Transactions

    Args:
        cointype: the coin shortname, example value 'BTC', 'LTC', 'DOGE'
        startdate - (optional) format 'YYYY-MM-DD'
        enddate - (optional) format 'YYYY-MM-DD'
    Returns:
        status - ok, error
        buyorders - array containing your coins buy order history
        sellorders - array containing your coins sell order history
    """

    def coin_transactions(self, cointype, startdate, enddate):
        return self._request("ro/my/transactions/:cointype", {
            "cointype": cointype,
            "startdate": startdate,
            "enddate": enddate
        })


    """Display Transactions

    Args:
        startdate - (optional) format 'YYYY-MM-DD'
        enddate - (optional) format 'YYYY-MM-DD'
    Returns:
        status - ok, error
        buyorders - array containing your coins buy order history
        sellorders - array containing your coins sell order history
    """

    def my_transactions(self, startdate, enddate):
        return self._request("ro/my/transactions", {
            "startdate": startdate,
            "enddate": enddate
        })
