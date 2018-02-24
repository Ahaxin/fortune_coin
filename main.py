import stellarTerm

trading_pairs=['xml_eurt','xml_cny','xml_xrp','xml_ltc','xml_eth','xml_btc']
TP='xml_btc'
for TP in trading_pairs:
    bids_list, asks_list=stellarTerm.extract(TP)
    print(bids_list)

