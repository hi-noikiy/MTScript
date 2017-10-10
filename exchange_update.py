from utils import print_log
from exchanges.liqui import LiquiExchange
from exchanges.bittrex import BittrexExchange
from exchanges.hitbtc import HitbtcExchange
from exchanges.poloniex import PoloniexExchange
from exchanges.bitz import BitzExchange
from exchanges.gateio import GateioExchange
from exchanges.bitstamp import BitstampExchange
from exchanges.nereax import NeraexExchange


if __name__ == '__main__':
    print_log("start sync exchanges...")

    le = LiquiExchange()
    le.post_result_batch()
    print_log("liqui done...")

    bt = BittrexExchange()
    bt.post_result_batch()
    print_log("bittrex done...")

    hb = HitbtcExchange()
    hb.post_result_batch()
    print_log("hitbtc done...")

    px = PoloniexExchange()
    px.post_result_batch()
    print_log("poloniex done...")

    bz = BitzExchange()
    bz.post_result_batch()
    print_log("Bit-Z done...")

    gt = GateioExchange()
    gt.post_result_batch()
    print_log("Gate.io done...")

    bs = BitstampExchange()
    bs.post_result_batch()
    print_log('Bitstamp done...')

    nx = NeraexExchange()
    nx.post_result_batch()
    print_log('Nereax done...')

    print_log("all exchanges synced...")
