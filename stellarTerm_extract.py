# Extract Trade Info from StellarTerm
import requests
import json
def stellarTerm_xlm_eurt():
    url = "https://horizon.stellar.org/order_book?selling_asset_type=native&buying_asset_type=credit_alphanum4&buying_asset_code=EURT&buying_asset_issuer=GAP5LETOV6YIE62YAM56STDANPRDO7ZFDBGSNHJQIYGGKSMOZAHOOS2S&c=0.17838799816662965"
    response = requests.get(url)
    content = response.content.decode()
    # Load BIDS List
    bids_list=json.loads(content)['bids']
    bid_price_list=[]
    for bid in bids_list:
        price_r_n =bid['price_r']['n']
        price_r_d =bid['price_r']['d']
        price     =bid['price']
        amount    =bid['amount']
        bid_price_list.append(price)
    # Load ASKS List
    asks_list=json.loads(content)['asks']
    ask_price_list=[]
    for ask in asks_list:
        price_r_n =ask['price_r']['n']
        price_r_d =ask['price_r']['d']
        price     =ask['price']
        amount    =ask['amount']
        ask_price_list.append(price)

    print ('Bids <=============> Asks')
    for n,g in zip(bid_price_list,ask_price_list):
        print (n + '\t\t\t' + g)
    return




