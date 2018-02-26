import stellarTerm
import binance
import okEX

trading_pairs=['xml_eurt','xml_cny','xml_xrp','xml_ltc','xml_eth','xml_btc','xrp_btc','eth_btc','ltc_btc']

for TP in trading_pairs:
    print("========== StellarTerm =========")
    bids_list, asks_list=stellarTerm.extract(TP)
    print(asks_list)
    print(bids_list)
    print("==========   Binance   =========")
    bids_list_c, asks_list_c=binance.extract(TP)
    print(asks_list_c)
    print(bids_list_c)
    print("==========   OKEX   =========")
    bids_list_b, asks_list_b=okEX.extract(TP)
    print(asks_list_b)
    print(bids_list_b)

