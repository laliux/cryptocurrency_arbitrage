import ccxt

from Exchange import Exchange
from crypto_trade import CryptoTradeAPI
from myutils import get_swapped_order
from order import Order

class CryptoExchange(Exchange):
    def __init__(self, exchange_id, api_key, secret):
        super(CryptoExchange, self).__init__()
        
        self.exchange_id = exchange_id
        self.name = exchange_id.upper()

        self.exchange = getattr(ccxt, exchange_id)({"enableRateLimit": True })
        self.markets = self.exchange.load_markets()        

        self.set_tradeable_pairs()

        self.trading_fee = 0.002

    def set_tradeable_pairs(self):
        exchange_markets = dict()

        exchange_markets['USDT'] = dict()
        exchange_markets['BTC'] = dict()
        exchange_markets['ETH'] = dict()
        
        exchange_markets['USDT'] = [ self.markets[key]['base'] for key in self.markets 
                                                        if self.markets[key]['quote'] in ['USDT'] ]

        exchange_markets['BTC'] = [ self.markets[key]['base'] for key in self.markets 
                                                        if self.markets[key]['quote'] in ['BTC'] ]

        exchange_markets['ETH'] = [ self.markets[key]['base'] for key in self.markets 
                                                        if self.markets[key]['quote'] in ['ETH'] ]     
        
        for pair in exchange_markets['USDT']:
            if pair in ['BCH','TUSD']:
                continue
        
            if pair in exchange_markets['BTC']:
                if pair in exchange_markets['ETH']:
                    self.tradeable_pairs.append((pair, 'ETH'))
                    self.tradeable_pairs.append((pair, 'BTC'))

                    self.tradeable_currencies.append(pair)
        
        self.tradeable_pairs.append(('ETH', 'BTC'))
        self.tradeable_pairs.append(('BTC', 'ETH'))

        self.tradeable_currencies.append('BTC')
        self.tradeable_currencies.append('ETH')    

    def get_depth(self, base, alt):
        book = {'bids': [], 'asks': []}
        """
        pair, swapped = self.get_validated_pair((base, alt))
        b,a = pair
        slug = b.lower() + "_" + a.lower()
        data = self.api.reqpublic('depth' + '/' + slug)
        if swapped:
            for ask in data['asks']:
                o = Order(float(ask[0]), float(ask[1]))
                bid = get_swapped_order(o)
                book['bids'].append(bid)
            for bid in data['bids']:
                o = Order(float(bid[0]), float(bid[1]))
                ask = get_swapped_order(o)
                book['asks'].append(ask)
        else:
            for bid in data['bids']:
                o = Order(float(bid[0]), float(bid[1]))
                book['bids'].append(o)
            for ask in data['asks']:
                o = Order(float(ask[0]), float(ask[1]))
                book['asks'].append(o)
        """
        return book

    def get_balance(self, currency):
        #funds = self.api.req('getinfo')['data']['funds']
        #return float(funds.get(currency.lower(), 0.0))
        return NotImplemented

    def get_all_balances(self):
        #funds = self.api.req('getinfo')['data']['funds']
        #balances = {k.upper() : float(v) for k,v in funds.items()}
        #return balances
        return NotImplemented

    def submit_order(self, gc, gv, rc, rv):
        return NotImplemented

    def confirm_order(self, orderID):
        return NotImplemented