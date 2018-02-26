# Extract Trade Info from StellarTerm
import requests
import json

def extract(TP):
    if TP =="xml_eurt":
        url = "https://horizon.stellar.org/order_book?selling_asset_type=native&buying_asset_type=credit_alphanum4&buying_asset_code=EURT&buying_asset_issuer=GAP5LETOV6YIE62YAM56STDANPRDO7ZFDBGSNHJQIYGGKSMOZAHOOS2S&c=0.17838799816662965"
        print("Trading Pair is XML<->EURT")
    elif TP == "xml_cny":
        url = "https://horizon.stellar.org/order_book?selling_asset_type=native&buying_asset_type=credit_alphanum4&buying_asset_code=CNY&buying_asset_issuer=GAREELUB43IRHWEASCFBLKHURCGMHE5IF6XSE7EXDLACYHGRHM43RFOX&c=0.9128589413221149"
        print("Trading Pair is XML<->CNY")
    elif TP == "xml_xrp":
        url = "https://horizon.stellar.org/order_book?selling_asset_type=credit_alphanum4&selling_asset_code=XRP&selling_asset_issuer=GA7FCCMTTSUIC37PODEL6EOOSPDRILP6OQI5FWCWDDVDBLJV72W6RINZ&buying_asset_type=native&c=0.3795148197759557"
        print("Trading Pair is XML<->XRP")
    elif TP == "xml_ltc":
        url = "https://horizon.stellar.org/order_book?selling_asset_type=credit_alphanum4&selling_asset_code=LTC&selling_asset_issuer=GC5LOR3BK6KIOK7GKAUD5EGHQCMFOGHJTC7I3ELB66PTDFXORC2VM5LP&buying_asset_type=native&c=0.37321711147845327"
        print("Trading Pair is XML<->LTC")
    elif TP == "xml_eth":
        url = "https://horizon.stellar.org/order_book?selling_asset_type=credit_alphanum4&selling_asset_code=ETH&selling_asset_issuer=GBDEVU63Y6NTHJQQZIKVTC23NWLQVP3WJ2RI2OTSJTNYOIGICST6DUXR&buying_asset_type=native&c=0.0799001525132561"
        print("Trading Pair is XML<->ETH")
    elif TP == "xml_btc":
        url = "https://horizon.stellar.org/order_book?selling_asset_type=native&buying_asset_type=credit_alphanum4&buying_asset_code=BTC&buying_asset_issuer=GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH&c=0.9643613563961166"
        print("Trading Pair is XML<->BTC")
    else:
        print("Currently not support this trading pairs",TP)
        return [],[]
    response = requests.get(url)
    content = response.content.decode()
    # Load BIDS List
    bids_list=json.loads(content)['bids']
    #bid_price_list=[]
    #for bid in bids_list:
    #    price_r_n =bid['price_r']['n']
    #    price_r_d =bid['price_r']['d']
    #    price     =bid['price']
    #    amount    =bid['amount']
        #bid_price_list.append(price)
    # Load ASKS List
    asks_list=json.loads(content)['asks']
    #ask_price_list=[]
    #for ask in asks_list:
    #    price_r_n =ask['price_r']['n']
    #    price_r_d =ask['price_r']['d']
    #    price     =ask['price']
    #    amount    =ask['amount']
    #    #ask_price_list.append(price)

    #print ('Bids <=============> Asks')
    #for n,g in zip(bid_price_list,ask_price_list):
    #    print (n + '\t\t\t' + g)
    return bids_list,asks_list




