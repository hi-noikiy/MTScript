from utils import print_log
from exchanges.binance import BinanceExchange
from exchanges.gateio import GateioExchange
from exchanges.kucoin import KucoinExchange
from exchanges.chaoex import ChaoexExchange


if __name__ == '__main__':
    print_log("start sync exchanges...")

    bn = BinanceExchange()
    bn.post_result_batch()
    print_log("Binance done...")

    gt = GateioExchange()
    gt.post_result_batch()
    print_log("Gate.io done...")

    kc = KucoinExchange()
    kc.post_result_batch()
    print_log("Kucoin done...")

    print_log("all exchanges synced...")
