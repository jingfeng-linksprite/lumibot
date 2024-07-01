from config import ALPACA_CONFIG
from lumibot.brokers import Alpaca
from lumibot.strategies import Strategy
from lumibot.traders import Trader

class SwingHigh(Strategy):
    data = []
    order_number = 0
    def initialize(self):
        self.set_market('NASDAQ')
        self.sleeptime = "60S"
        self.minutes_before_closing=300
       

    def before_market_opens(self):
        print("before market open")

    def on_trading_iteration(self):
        print("on trading iteratio, doing strategy")


    def before_market_closes(self):
        print("before market close")


    def after_market_closes(self):
        self.log_message("The market is closed, after market closes")

    def on_abrupt_closing(self):
        self.log_message("Abrupt closing")


if __name__ == "__main__":
    broker = Alpaca(ALPACA_CONFIG)
    strategy = SwingHigh(broker=broker)
    trader = Trader()
    trader.add_strategy(strategy)
    trader.run_all()








        
