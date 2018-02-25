import stellarTerm
import binance
import okEX

trading_pairs=['xml_eurt','xml_cny','xml_xrp','xml_ltc','xml_eth','xml_btc','xrp_btc']

for TP in trading_pairs:
#    print("========== StellarTerm =========")
#    bids_list, asks_list=stellarTerm.extract(TP)
#    print(bids_list)
#    print(asks_list)
#    print("==========   Binance   =========")
#   bids_list_b, asks_list_b=binance.extract(TP)
#   print(bids_list_b)
#    print(asks_list_b)
    print("==========   OKEX   =========")
    bids_list_b, asks_list_b=okEX.extract('xml_btc')
#    print(bids_list_b)
#    print(asks_list_b)

