import config

from Broker import Broker
from CryptoExchange import CryptoExchange

def create_brokers(mode, pairs, exchangeNames):
    # returns an array of Broker objects
    brokers = []
    for name in exchangeNames:
        if (name == 'binance'):
            xchg = CryptoExchange('binance', config.BINANCE_KEY, config.BINANCE_SECRET)
        else:
            print('Exchange ' + name + ' not supported!')
            continue
        print('%s initialized' % (xchg.name))

        broker = Broker(mode, xchg)
        if mode == 'BACKTEST':
#            broker.balances = config.PAPER_BALANCE
            broker.balances = broker.xchg.get_all_balances() # use real starting balances.
        brokers.append(broker)
    return brokers

def get_assets(brokers):
    # prints out total assets held across all brokers
    assets = {}
    for broker in brokers:
        for currency, balance in broker.balances.items():
            if currency in assets:
                assets[currency] += balance
            elif balance > 0.0:
                assets[currency] = balance
    return assets

def print_assets(brokers):
    print(get_assets(brokers))
