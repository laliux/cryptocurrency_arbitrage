# represents a single order object
# very simple data structure!

class Order(object):
    def __init__(self, price, volume, order_type=None, pair=None, orderID=None, timestamp=None):
        """
        markets are usually expressed in terms of BASE_ALT where you buy
        and sell units of BASE with ALT.
        price = price (in units alt) of 1 unit of base
        volume = total volume of base desired
        orderID = necessary for tracking & cancelling & ignoring already executed orders when backtesting
        """
        self.p = price
        self.v = volume
        self.order_type = order_type # buy or sell
        self.pair = pair # market we are trading on
        self.id = orderID
        self.time = timestamp

    def info(self):
        return 'Type: %s, pair: %s, price: %0.5f' % (self.order_type, self.pair, self.p)