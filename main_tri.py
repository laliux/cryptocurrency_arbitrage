from TriangularArbitrageBot import TriangularArbitrageBot
from broker_utils import create_brokers
import config_tri as config

brokers = create_brokers('PAPER', config.PAIRS, config.EXCHANGES)
bot = TriangularArbitrageBot(config, brokers)

#bot.start()

