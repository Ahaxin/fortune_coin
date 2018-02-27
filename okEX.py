# Extract Trade Info from Binance
import requests
import json


def extract(TP):
    if TP == "eth_btc":
        url = "https://www.okex.com/v2/markets/eth_btc/depth"
#        print("Trading Pair is ETH<->BTC")
    elif TP == "xrp_btc":
        url = "https://www.okex.com/v2/markets/xrp_btc/depth"
#        print("Trading Pair is XRP<->BTC")
    elif TP == "xml_btc":
        url = "https://www.okex.com/v2/markets/xlm_btc/depth"
#       print("Trading Pair is XML<->BTC")
    elif TP == "ltc_btc":
        url = "https://www.okex.com/v2/markets/ltc_btc/depth"
#        print("Trading Pair is LTC<->BTC")
    else:
#        print("Currently not support this trading pairs", TP)
        return [], [],0
    response = requests.get(url)
    content = response.content.decode()
    # Load BIDS List
    offer_list = json.loads(content)['data']
    asks_list=offer_list['asks']
    bids_list=offer_list['bids']
    for item in asks_list:
        item['amount']=item.pop('totalSize')
    for item in bids_list:
        item['amount']=item.pop('totalSize')
    return bids_list, asks_list,1
