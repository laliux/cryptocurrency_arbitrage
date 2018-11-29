
import sys

from TriangularArbitrageBot import TriangularArbitrageBot
from broker_utils import create_brokers
import config_tri as config

if __name__ == "__main__":
    try:
        brokers = create_brokers('PAPER', config.PAIRS, config.EXCHANGES)
        bot = TriangularArbitrageBot(config, brokers)

        bot.start()
    except KeyboardInterrupt:
        sys.exit(0)