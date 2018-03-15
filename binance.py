# Extract Trade Info from Binance
import requests
import json

def extract(TP):
    if TP =="eth_btc":
        url = "https://www.binance.com/api/v1/depth?symbol=ETHBTC"
#        print("Trading Pair is ETH<->BTC")
    elif TP == "xrp_btc":
        url = "https://www.binance.com/api/v1/depth?symbol=XRPBTC"
#        print("Trading Pair is XRP<->BTC")
    elif TP == "xlm_btc":
        url = "https://www.binance.com/api/v1/depth?symbol=XLMBTC"
#        print("Trading Pair is XML<->BTC")
    elif TP == "ltc_btc":
        url = "https://www.binance.com/api/v1/depth?symbol=LTCBTC"
#        print("Trading Pair is LTC<->BTC")
    else:
#        print("Currently not support this trading pairs %s",TP)
        return [],[],0
    response = requests.get(url)
    content = response.content.decode()
    # Load BIDS List
    bids=json.loads(content)['bids']
    bids_list=[]
#    print(type(bids_list))
    for items in bids:
        bids_pair={}
        bids_pair['price']=items[0]
        bids_pair['amount']=items[1]
        bids_list.append(bids_pair)
#    print(bids_list)
#    print(bids)

    asks=json.loads(content)['asks']
    asks_list=[]
    for items in asks:
        asks_pair={}
        asks_pair['price']=items[0]
        asks_pair['amount']=items[1]
        asks_list.append(asks_pair)
#    print(asks_list)
#    print(asks)
    return bids_list,asks_list,1
