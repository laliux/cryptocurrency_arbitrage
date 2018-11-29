#
# Global user settings
# DO NOT let this file fall into the wrong hands!

TICK_DIR = './data' # path to folder containing serialized historical tick data

# reference values in USD for each currency
# this is approximate. Unless values are a magnitude away from true values, I should be fine
# The main_pair purpose of this is to just pass by opportunities that net insignificant profit
VALUE_REF = {
             'BTC': 4200.0,       # bitcoin
             'LTC': 33.0,       # litecoin
             'ETH': 117.0,       # ether
             'DOGE': 0.0015,     # dogecoin
             'PPC': 4.00,       # peercoin
             'NMC':3.90,        # namecoin
             'QRK': 0.07,    # quarkcoin
             'NXT':0.056,       # nxt
             'WDC':0.18         # worldcon
             }

# I use this in arbitrage -> do not attempt trade unless profit > 1 cent
PROFIT_THRESH = { k:0.01/v for k,v in VALUE_REF.items() }
PAPER_BALANCE = {k:20/v for k,v in VALUE_REF.items()} # for 7 exchanges, have
#PAPER_BALANCE = {'BTC':0.3, 'LTC':1.0, 'DOGE':10000, }

# a better metric of whether I should go after a trade or not should be instead based on
# the amount of money I have to move to perform the trade.
# i.e. I don't want to move 1.0 BTC (1000 USD) just to profit 1 cent!!!
# BTC risk is how much BTC I expect to profit per BTC I move.
# In a paired trade, I'm really moving twice as much value on both ends.
BTC_RISK = 0.001 # as you grow more confident in the stability of the trading bot, you can increase riskiness by decreasing this number.

# COINEX API
COINEX_API_KEY = "yourkeyhere"
COINEX_SECRET = "yoursecretkeyhere"

BINANCE_KEY = 'foo'
BINANCE_SECRET = 'bar'
