#!/usr/bin/python3

from coinspot import CoinSpot
import pprint

_api_key = ''
_api_secret = ''

#coin=CoinSpot(_api_key,_api_secret)
#pprint.pprint(coin)
#print("My Balance")
#pprint.pprint(coin.my_balances())

'''
Purchase quotes for Bitcoin
'''

#print("Quotes to buy Bitcoin")
#pprint.pprint(coin.quote_buy('BTC','1'))

'''
Sell quotes for Bitcoin

'''
#print("Quotes to sell Bitcoin")
#pprint.pprint(coin.quote_sell('BTC','1'))

'''
My crypto orders
'''
#print("My crypto orders")
#pprint.pprint(coin.my_orders())

'''
Litecoin orders
'''
#print("Litecoin orders")
#print(coin.orders('LTC'))

'''
Latest cryptos
'''
#print("Latest cryptos")
#print(coin.latest())

#coin.my_coin_send('DOGE','DMJWtt4txj8XhfumdHNAW3LJLgRtstyUvD','2')
#print("Sell order for DRGN")
#acoin.my_sell_cancel('5ef9d8644b2a0218ea91f86e')
#coin.my_sell('DRGN','1','.5')
#coin.my_sell_cancel('5ef9d8644b2a0218ea91f86e')
#print(coin.my_coin_send("BTC",'3PKkgzspAToLLYSyfV78m3NFsW6PigyaiT',4))
#print(coin.my_coin_deposit('LTC'))


print('''





#  ~██████╗~██████╗~██╗███╗~~~██╗███████╗██████╗~~██████╗~████████╗~~~~~█████╗~██████╗~██╗
#  ██╔════╝██╔═══██╗██║████╗~~██║██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝~~~~██╔══██╗██╔══██╗██║
#  ██║~~~~~██║~~~██║██║██╔██╗~██║███████╗██████╔╝██║~~~██║~~~██║~~~~~~~███████║██████╔╝██║
#  ██║~~~~~██║~~~██║██║██║╚██╗██║╚════██║██╔═══╝~██║~~~██║~~~██║~~~~~~~██╔══██║██╔═══╝~██║
#  ╚██████╗╚██████╔╝██║██║~╚████║███████║██║~~~~~╚██████╔╝~~~██║~~~~~~~██║~~██║██║~~~~~██║
#  ~╚═════╝~╚═════╝~╚═╝╚═╝~~╚═══╝╚══════╝╚═╝~~~~~~╚═════╝~~~~╚═╝~~~~~~~╚═╝~~╚═╝╚═╝~~~~~╚═╝
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')



print("Select an option: \n")
print("1. Search Coin Deposit Address")
print("2. Deposit Coins")
print("3. Display Transactions")
print("4. Display Buy/Sell Orders")
print("5. Display Coin Transactions")
print("6. Cancel Sell Order")
print("7. Cancel Buy Order")
print("8. Show latest prices")
print("9. Display Buy quote")
print("0. Display Sell quote")
print("q. Quit")

def CoinDepositAddress():
        print("Enter Coin Ticker:")
        address = input()
        pprint.pprint(coin.my_coin_deposit(address))
def DepositCoin():
        print("deleted")
def SendCrypto():
        print("Enter cyrpto address")
        address = input()
        coin.my_coin_send("BTC",address,"1.03846462")
        print("Crypto sent!")
def DisplayTransactions():
        print("Enter Start date (YYYY-MM-DD:")
        start_date = input()
        print("Enter End date (YYYY-MM-DD:")
        end_date = input()
        pprint.pprint(coin.my_transactions(start_date,end_date))
def CreateBuyOrder():
        print("Enter Coin:")
        coin=input()
        print("Enter Rate:")
        rate=input()
        print("Enter Amount:")
        amount=input()
        pprint.pprint(coin.my_buy(coin,amount,rate))
def CreateSellOrder():
        print("Enter Coin")
        coin=input()
        print("Enter Rate")
        rate=input()
        print("Enter Amount")
        amount=input()
        pprint.pprint(coin.my_sell(coin,amount,rate))
def CancelSellOrder():
        print("Enter Order ID")
        id = input()
        coin.my_sell_cancel(id)
def CancelBuyOrder():
        print("Enter Order ID")
        id = input()
        coin.my_buy_cancel(id)
def ShowOrders():
        print("My Buy/Sell Orders")
        pprint.pprint(coin.my_orders())
def DisplayCoinTransactions():
        print("Enter Coin:")
        cointype=input()
        print("Enter Start date (YYYY-MM-DD:")
        start_date = input()
        print("Enter End date (YYYY-MM-DD:")
        end_date = input()
        pprint.pprint(coin.coin_transactions(cointype,start_date,end_date))
def ShowLatest():
        print("Latest Coin prices")
        pprint.pprint(coin.latest())
def BuyQuote():
        print("Enter Coin:")
        crypto=input()
        print("Enter Amount:")
        amount=input()
        print("Quotes to buy Coin")
        pprint.pprint(coin.quote_buy(crypto,amount))
def SellQuote():
        print("Enter Coin:")
        crypto=input()
        print("Enter Amount:")
        amount=input()
        print("Quotes to sell Coin")
        pprint.pprint(coin.quote_sell(crypto,amount))
def CleanupAndQuit():
        print("byez")

menuchoices = {'1':CoinDepositAddress, '2':DepositCoin, '3':DisplayTransactions, '4':ShowOrders, '5':DisplayCoinTransactions, '6':CancelSellOrder, '7':CancelBuyOrder, '8':ShowLatest, '9':BuyQuote, '0':SellQuote, 'q':CleanupAndQuit}
ret = menuchoices[input()]()
#if ret is None:
    #print("Please enter a valid menu choice!")
#menuchoices['q']()