#!/usr/bin/python3

from coinspot import CoinSpot
import sys, pprint, subprocess, config

sys.path.append(".")

_api_key = config._api_key
_api_secret = config._api_secret

coin=CoinSpot(_api_key,_api_secret)
print('''





  ~██████╗~██████╗~██╗███╗~~~██╗███████╗██████╗~~██████╗~████████╗~~~~~█████╗~██████╗~██╗
  ██╔════╝██╔═══██╗██║████╗~~██║██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝~~~~██╔══██╗██╔══██╗██║
  ██║~~~~~██║~~~██║██║██╔██╗~██║███████╗██████╔╝██║~~~██║~~~██║~~~~~~~███████║██████╔╝██║
  ██║~~~~~██║~~~██║██║██║╚██╗██║╚════██║██╔═══╝~██║~~~██║~~~██║~~~~~~~██╔══██║██╔═══╝~██║
  ╚██████╗╚██████╔╝██║██║~╚████║███████║██║~~~~~╚██████╔╝~~~██║~~~~~~~██║~~██║██║~~~~~██║
  ~╚═════╝~╚═════╝~╚═╝╚═╝~~╚═══╝╚══════╝╚═╝~~~~~~╚═════╝~~~~╚═╝~~~~~~~╚═╝~~╚═╝╚═╝~~~~~╚═╝
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

print("---------------------------------")
print("Select an option:")
print("---------------------------------\n")
print("1. Coin Address")
print("2. Open Orders")
print("3. Transactions")
print("4. Buy/Sell Orders")
print("5. Coin Transactions")
print("6. Cancel Sell Order")
print("7. Cancel Buy Order")
print("8. latest prices")
print("9. Buy quote")
print("a. Affiliate Payments")
print("0. Sell quote")
print("o. My Orders")
print("h. Orders History")
print("b. My Balances")
print("g. Place Buy Order")
print("r. Coin Balance")
print("p. Place Sell Order")
print("q. Quit\n\n")
print("----------------------------------\n")

def CoinDepositAddress():
        subprocess.call('clear')
        print("Enter Coin Ticker:")
        address = input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("Coin Deposit Address for" ,address)
        print("----------------------------------------------------------\n")
        pprint.pprint(coin.my_coin_deposit(address))
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def AffiliatePayments():
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("Affiliate Payments")
        print("----------------------------------------------------------\n")
        pprint.pprint(coin.affiliate_payments())
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def DisplayMyOrders():
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("My Orders")
        print("----------------------------------------------------------\n")
        pprint.pprint(coin.my_orders())
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def CoinBalance():
        subprocess.call('clear')
        crypto=input("Enter Coin: ")
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("Coin Balance for ", crypto)
        print("\n----------------------------------------------------------\n")
        pprint.pprint(coin.my_coin_balance(crypto))
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def DisplayOrdersHistory():
        subprocess.call('clear')
        cointype = input("Enter Coin: ")
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("Order History")
        print("----------------------------------------------------------\n")
        pprint.pprint(coin.orders_history(cointype))
        print("----------------------------------------------------------\n")

def DisplayBalance():
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("My Balance")
        print("----------------------------------------------------------\n")
        pprint.pprint(coin.my_balances())
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def DisplayOpenOrders():
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        cointype = input("Enter Coin: ")
        subprocess.call('clear')
        print("----------------------------------------------------------\n")
        print("Open Orders")
        print("----------------------------------------------------------\n")
        pprint.pprint(coin.orders(cointype))
        print("\n----------------------------------------------------------\n")
        print("\n\n")
        
def DisplayTransactions():
        subprocess.call('clear')
        print("Enter Start date (YYYY-MM-DD:)")
        start_date = input()
        print("Enter End date (YYYY-MM-DD:)")
        end_date = input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("\nTransactions")
        print("\n----------------------------------------------------------\n")
        pprint.pprint(coin.my_transactions(start_date,end_date))
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def PlaceBuyOrder():
        subprocess.call('clear')
        print("Enter Coin:")
        crypto=input()
        print("Enter Amount:")
        amount=input()
        print("Enter Rate:")
        rate=input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("\nNew Buy Order")
        print("----------------------------------------------------------\n")
        pprint.pprint(coin.my_buy(crypto,amount,rate))
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def PlaceSellOrder():
        subprocess.call('clear')
        print("Enter Coin")
        crypto=input()
        print("Enter Amount")
        amount=input()
        print("Enter Rate")
        rate=input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("\nNew Sell Order")
        print("\n----------------------------------------------------------\n")
        pprint.pprint(coin.my_sell(crypto,amount,rate))
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def CancelSellOrder():
        subprocess.call('clear')
        print("Enter Order ID")
        id = input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("\nCancel Sell Order")
        print("----------------------------------------------------------\n")
        pprint.pprint(coin.my_sell_cancel(id))
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def CancelBuyOrder():
        subprocess.call('clear')
        print("Enter Order ID")
        id = input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        pprint.pprint(coin.my_buy_cancel(id))
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def ShowOrders():
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------\n")
        print("\nMy Buy/Sell Orders")
        print("----------------------------------------------------------")
        pprint.pprint(coin.my_orders())
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def DisplayCoinTransactions():
        subprocess.call('clear')
        print("Enter Coin:")
        cointype=input()
        print("Enter Start date (YYYY-MM-DD:)")
        start_date = input()
        print("Enter End date (YYYY-MM-DD:)")
        end_date = input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------")
        print("\nCoin Transactions for ", cointype)
        print("----------------------------------------------------------\n")
        pprint.pprint(coin.coin_transactions(cointype,start_date,end_date))
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def ShowLatest():
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------")
        print("\nLatest Coin prices\n\n")
        print("----------------------------------------------------------")
        pprint.pprint(coin.latest())
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def BuyQuote():
        subprocess.call('clear')
        print("Enter Coin:")
        crypto=input()
        print("Enter Amount:")
        amount=input()
        subprocess.call('clear')
        print("----------------------------------------------------------")
        print("Buy Quotes for ",amount , " ", crypto)
        print("----------------------------------------------------------")
        pprint.pprint(coin.quote_buy(crypto,amount))
        print("\n----------------------------------------------------------\n")
        print("\n\n")


def MyBuy():
        subprocess.call('clear')
        print("Enter Coin:")
        crypto=input()
        print("Enter Amount:")
        amount=input()
        print("Enter Rate:")
        rate=input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------")
        print("\nPlacing Buy Order for ", amount, " ", crypto)
        print("\n----------------------------------------------------------")
        pprint.pprint(coin.my_buy(crypto, amount, rate))
        print("\n----------------------------------------------------------")
        print("\n\n")
        

def MySell():
        subprocess.call('clear')
        print("Enter Coin:")
        crypto=input()
        print("Enter Amount:")
        amount=input()
        print("Enter Rate:")
        rate=input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------")
        print("\nSelling ", amount, crypto)
        print("\n----------------------------------------------------------")
        pprint.pprint(coin.my_sell(crypto, amount, rate))
        print("\n----------------------------------------------------------")
        print("\n\n")

def SellQuote():
        subprocess.call('clear')
        print("Enter Coin:")
        crypto=input()
        print("Enter Amount:")
        amount=input()
        subprocess.call('clear')
        print("\n\n----------------------------------------------------------")
        print("Quotes to sell Coin")
        print("----------------------------------------------------------")
        pprint.pprint(coin.quote_sell(crypto,amount))
        print("\n----------------------------------------------------------\n")
        print("\n\n")

def CleanupAndQuit():
        print("byez")

menuchoices = {'1':CoinDepositAddress, '2':DisplayOpenOrders, '3':DisplayTransactions, '4':ShowOrders, '5':DisplayCoinTransactions, '6':CancelSellOrder, '7':CancelBuyOrder, '8':ShowLatest, '9':BuyQuote, '0':SellQuote, 'h':DisplayOrdersHistory, 'o':DisplayMyOrders, 'b':DisplayBalance, 'q':CleanupAndQuit, 'g': MyBuy, 'p' :MySell, 'r':CoinBalance,'a': AffiliatePayments }

ret = menuchoices[input("Option: ")]()

#if ret is None:
    #print("Please enter a valid menu choice!")
#menuchoices['q']()
