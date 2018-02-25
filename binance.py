# Extract Trade Info from Binance
import requests
import json

def extract(TP):
    if TP =="eth_btc":
        url = "https://www.binance.com/api/v1/depth?symbol=ETHBTC"
        print("Trading Pair is ETH<->BTC")
    elif TP == "xrp_btc":
        url = "https://www.binance.com/api/v1/depth?symbol=XRPBTC"
        print("Trading Pair is XRP<->BTC")
    elif TP == "xml_btc":
        url = "https://www.binance.com/api/v1/depth?symbol=XLMBTC"
        print("Trading Pair is XML<->BTC")
    elif TP == "ltc_btc":
        url = "https://www.binance.com/api/v1/depth?symbol=LTCBTC"
        print("Trading Pair is LTC<->BTC")
    else:
        print("Currently not support this trading pairs %s",TP)
        return [],[]
    response = requests.get(url)
    content = response.content.decode()
    # Load BIDS List
    bids_list=json.loads(content)['bids']
    bid_price_list=[]
    for bid in bids_list:
        price     =bid[0]
        amount    =bid[1]
        bid_price_list.append(price)
    # Load ASKS List
    asks_list=json.loads(content)['asks']
    ask_price_list=[]
    for ask in asks_list:
        price     =ask[0]
        amount    =ask[1]
        ask_price_list.append(price)

    #print ('Bids <=============> Asks')
    #for n,g in zip(bid_price_list,ask_price_list):
    #    print (n + '\t\t\t' + g)
    return bids_list,asks_list
