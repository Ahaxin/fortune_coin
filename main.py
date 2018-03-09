import stellarTerm
import binance
import okEX
import misc
import datetime
import sys
import time
import progressbar


trading_pairs=['xml_eurt','xml_cny','xml_xrp','xml_ltc','xml_eth','xml_btc','xrp_btc','eth_btc','ltc_btc']
profile_TPs = ['xml_btc','xrp_btc','eth_btc','ltc_btc'] # trading pairs on multiple exchanges
#profile_TPs = ['xml_btc'] # trading pairs on multiple exchanges

totalTimes = 10

largest_a_n1   = {}
largest_b_n1   = {}
lplatform_b_n1  = {}
lplatform_a_n1  = {}
smallest_a_n1   = {}
smallest_b_n1   = {}
splatform_a_n1  = {}
splatform_b_n1  = {}
still_cnt ={}
cnt_enable={}
cnt_enable_d1={}
still_stop_time={}
still_start_time={}
start = 0
for TP in profile_TPs:
    largest_a_n1[TP]    = ''
    largest_b_n1[TP]    = ''
    lplatform_b_n1[TP]  = ''
    lplatform_a_n1[TP]  = ''
    smallest_a_n1[TP]   = ''
    smallest_b_n1[TP]   = ''
    splatform_a_n1[TP]  = ''
    splatform_b_n1[TP]  = ''
    still_cnt[TP]       = 0
    still_start_time[TP]= ''
    still_start_time[TP] = ''
    cnt_enable[TP]       = 0
    cnt_enable_d1[TP]    = 0
pbar = progressbar.ProgressBar()
pbar.start(totalTimes)

timestr = time.strftime("%Y%m%d_%H%M%S")

for running_times in range(totalTimes):
    for TP in profile_TPs:
        f = open(timestr+'_test_data_'+TP+'_'+str(totalTimes)+'.txt','a')
        bids_list_ST, asks_list_ST,valid_ST=stellarTerm.extract(TP)
        bids_list_BN, asks_list_BN,valid_BN=binance.extract(TP)
        bids_list_OK, asks_list_OK,valid_OK=okEX.extract(TP)
        if (int(valid_BN)+int(valid_ST)+int(valid_OK)>1): #More than one trading platform supports current trading pair
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
            if (largest_a == largest_a_n1[TP]) and (largest_b==largest_b_n1[TP]) and (splatform_a_n1[TP] == splatform_a) and (splatform_b_n1[TP] == splatform_b):
                if cnt_enable[TP] == 0:
                    still_start_time[TP] =datetime.datetime.now()
                time.sleep(1)
                still_cnt[TP] = still_cnt[TP] + 1
                cnt_enable_d1[TP]=cnt_enable[TP]
                cnt_enable[TP] = 1
                start = 1
                f.write("%s %s %s %.10f \t %s %.10f \t %s %.10f \t %s %.10f Ask_Diff: %.10f Bid_Diff: %.10f \n"%(datetime.datetime.now(),TP,lplatform_a,float(largest_a),lplatform_b,float(largest_b),
                      splatform_a,float(smallest_a),splatform_b,float(smallest_b), (float(largest_a)-float(smallest_a)),(float(largest_b)-float(smallest_b))))
            else:

                if (cnt_enable_d1[TP]==0) and start == 1:
                    still_stop_time[TP] =datetime.datetime.now()
                    f.write("From %s to %s: Counter:%s \n"%(still_start_time[TP],still_stop_time[TP],still_cnt[TP]))
                f.write("%s %s %s %.10f \t %s %.10f \t %s %.10f \t %s %.10f Ask_Diff: %.10f Bid_Diff: %.10f \n"%(datetime.datetime.now(),TP,lplatform_a,float(largest_a),lplatform_b,float(largest_b),
                      splatform_a,float(smallest_a),splatform_b,float(smallest_b), (float(largest_a)-float(smallest_a)),(float(largest_b)-float(smallest_b))))
                still_cnt[TP] = 0
                cnt_enable_d1[TP]=cnt_enable[TP]
                cnt_enable[TP] = 0
                start = 1

            largest_a_n1[TP]    = largest_a
            largest_b_n1[TP]    = largest_b
            lplatform_b_n1[TP]  = lplatform_b
            lplatform_a_n1[TP]  = lplatform_a
            smallest_a_n1[TP]   = smallest_a
            smallest_b_n1[TP]   = smallest_b
            splatform_a_n1[TP]  = splatform_a
            splatform_b_n1[TP]  = splatform_b
  #          if cnt_enable[TP] == 1 and cnt_enable_d1[TP] != 1 :
   #             still_stop_time[TP] =datetime.datetime.now()
   #             f.write("From %s to %s: Counter:%s \n"%(still_start_time[TP],still_stop_time[TP],still_cnt[TP]))


    #        print(datetime.datetime.now(),TP,lplatform_a,largest_a,"\t",lplatform_b,largest_b,"\t",
    #              splatform_a,smallest_a,"\t",splatform_b,smallest_b,"\t""Ask_Diff:",float(largest_a)-float(smallest_a),"\t""Bid_Diff:",float(largest_b)-float(smallest_b))
            f.close()
        else:
            print("Only one or None platform supports current trading pair yet!")
    pbar.update(running_times+1)
pbar.finish()

