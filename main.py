import stellarTerm
import binance
import okEX
import misc
import datetime

trading_pairs=['xml_eurt','xml_cny','xml_xrp','xml_ltc','xml_eth','xml_btc','xrp_btc','eth_btc','ltc_btc']
profile_TPs = ['xml_btc','xrp_btc','eth_btc','ltc_btc'] # trading pairs on multiple exchanges
f = open('test_data.txt','w')
for running_times in range(100000):
    for TP in profile_TPs:
    #    print("========== StellarTerm =========")
        bids_list_ST, asks_list_ST,valid_ST=stellarTerm.extract(TP)
    #    print(asks_list_ST)
    #    print(bids_list_ST)
    #    print("==========   Binance   =========")
        bids_list_BN, asks_list_BN,valid_BN=binance.extract(TP)
    #    print(asks_list_BN)
    #    print(bids_list_BN)
    #    print("==========   OKEX   =========")
        bids_list_OK, asks_list_OK,valid_OK=okEX.extract(TP)
    #    print(asks_list_OK)
    #    print(bids_list_OK)
        if (int(valid_BN)+int(valid_ST)+int(valid_OK)>1): #More than one trading platform supports current trading pair
     #       print("More than one trading platform supports current trading pair ",TP,(int(valid_BN)+int(valid_ST)+int(valid_OK)))
     #       if valid_ST: print("ST:",asks_list_ST[0]['price'],":",float(asks_list_ST[0]['amount']),"\t\t\t",bids_list_ST[0]['price'],":",bids_list_ST[0]['amount'])
     #       if valid_BN: print("BN:",asks_list_BN[0]['price'],":",float(asks_list_BN[0]['amount']),"\t\t\t",bids_list_BN[0]['price'],":",bids_list_BN[0]['amount'])
     #       if valid_OK: print("OK:",asks_list_OK[0]['price'],":",float(asks_list_OK[0]['amount']),"\t\t\t",bids_list_OK[0]['price'],":",bids_list_OK[0]['amount'])
            if valid_ST:
                asks_price_ST_1 = asks_list_ST[0]['price']
                bids_price_ST_1 = bids_list_ST[0]['price']
            else:
                asks_price_ST_1 = '0'
                bids_price_ST_1 = '0'

            if valid_BN:
                asks_price_BN_1 = asks_list_BN[0]['price']
                bids_price_BN_1 = bids_list_BN[0]['price']
            else:
                asks_price_BN_1 = '0'
                bids_price_BN_1 = '0'

            if valid_OK:
                asks_price_OK_1 = asks_list_OK[0]['price']
                bids_price_OK_1 = bids_list_OK[0]['price']
            else:
                asks_price_OK_1 = '0'
                bids_price_OK_1 = '0'

            largest_a,lplatform_a =misc.largest(asks_price_ST_1,asks_price_BN_1,asks_price_OK_1)
            largest_b,lplatform_b =misc.largest(bids_price_ST_1,bids_price_BN_1,bids_price_OK_1)
            smallest_a,splatform_a=misc.smallest(asks_price_ST_1,asks_price_BN_1,asks_price_OK_1)
            smallest_b,splatform_b=misc.smallest(bids_price_ST_1,bids_price_BN_1,bids_price_OK_1)

    #        print(datetime.datetime.now(),TP,lplatform_a,largest_a,"\t",lplatform_b,largest_b,"\t",
    #              splatform_a,smallest_a,"\t",splatform_b,smallest_b,"\t""Ask_Diff:",float(largest_a)-float(smallest_a),"\t""Bid_Diff:",float(largest_b)-float(smallest_b))
            f.write("%s %s %s %s \t %s %s \t %s %s \t %s %s Ask_Diff: %s Bid_Diff: %s \n"%(datetime.datetime.now(),TP,lplatform_a,largest_a,lplatform_b,largest_b,
                  splatform_a,smallest_a,splatform_b,smallest_b, (float(largest_a)-float(smallest_a)),(float(largest_b)-float(smallest_b))))
        else:
            print("Only one or None platform supports current trading pair yet!")

f.close()
