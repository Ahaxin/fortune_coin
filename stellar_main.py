import stellarTerm
import misc
import datetime
import sys
import time
import progressbar
from coinmarketcap import Market
coinmarketcap = Market()

C_xlm_naobtc = 500
C_xlm_tempo  = 500
C_max_trade_xlm = 200
tradable_xlm_naobtc = C_max_trade_xlm
tradable_xlm_tempo  = C_max_trade_xlm
btc_naobtc = 0.00003312*100
eur_tempo  = 0.24*100
real_amount_to_buy =0
real_amount_to_sell=0


r_xlm_naobtc = 800
r_xlm_tempo  = 800

profile_TPs = ['xml_btc','xml_eurt'] # trading pairs on multiple exchanges
thres_bot_detect = 5 #to avoid offers' amount smaller than 50

totalTimes = 10

pbar = progressbar.ProgressBar()
pbar.start(totalTimes)


timestr = time.strftime("%Y%m%d_%H%M%S")
f = open(timestr+'_action_log__'+str(totalTimes)+'.txt','a')
d = open(timestr+'_data_log__'+str(totalTimes)+'.txt','a')

for running_times in range(totalTimes):
    LOG_TIME = str(datetime.datetime.now())
    realtime_btc_price = coinmarketcap.ticker('bitcoin', convert='EUR')
    realtime_btc_price_in_eur = realtime_btc_price[0]['price_eur']
    #print(realtime_btc_price[0]['price_eur'])

    bids_list_BTC, asks_list_BTC,valid_BTC=stellarTerm.extract('xml_btc')
    bids_list_EUR, asks_list_EUR,valid_EUR=stellarTerm.extract('xml_eurt')

    # To avoid the offer with amount smaller than 50
    #if (bids_list_BTC[0]['amount'] < thres_bot_detect) or (asks_list_BTC[0]['amount'] <thres_bot_detect) or (bids_list_EUR[0]['amount'] < thres_bot_detect) or (asks_list_EUR[0]['amount'] <thres_bot_detect):
        #continue
        #print time + INFO

    bid_price_BTC = float(bids_list_BTC[0]['price'])*float(realtime_btc_price_in_eur)
    ask_price_BTC = float(asks_list_BTC[0]['price'])*float(realtime_btc_price_in_eur)
    bid_amount_BTC =float(bids_list_BTC[0]['amount'])
    ask_amount_BTC =float(asks_list_BTC[0]['amount'])
    bid_price_EUR = float(bids_list_EUR[0]['price'])
    ask_price_EUR = float(asks_list_EUR[0]['price'])
    bid_amount_EUR =float(bids_list_EUR[0]['amount'])
    ask_amount_EUR =float(asks_list_EUR[0]['amount'])

    d.write("%s: bid_price_BTC: %10f bid_amount_BTC: %10f ask_price_BTC: %10f ask_amount_BTC: %10f bid_price_EUR: %10f bid_amount_EUR: %10f ask_price_EUR: %10f ask_amount_EUR: %10f \n"%(LOG_TIME,bid_price_BTC,bid_amount_BTC,ask_price_BTC,ask_amount_BTC,bid_price_EUR,bid_amount_EUR,ask_price_EUR,ask_amount_EUR))
    state = []
    MSG_INFO={}
    MSG_INFO['0'] = '[0] bid_price_BTC > ask_price_EUR'
    MSG_INFO['1'] = '[1] bid_price_EUR > ask_price_BTC'
    MSG_INFO['2'] = '[2] bid_price_EUR > bid_price_BTC'
    MSG_INFO['3'] = '[3] bid_price_EUR < bid_price_BTC'
    MSG_INFO['4'] = '[4] ask_price_EUR < ask_price_BTC'
    MSG_INFO['5'] = '[5] ask_price_EUR > ask_price_BTC'
    MSG_INFO['6'] = '[6] undefined state              '

    if (bid_price_BTC > ask_price_EUR):
    #    INFO = '[0] Sell BTC and Buy EUR   '
    #    MSG_INFO[0] = '[0] bid_price_BTC > ask_price_EUR'
        state.append('0')
    if (bid_price_EUR > ask_price_BTC):
    #    INFO = '[1] Sell EUR and Buy BTC   '
     #   MSG_INFO[1] = '[1] bid_price_EUR > ask_price_BTC'
        state.append('1')
    if (ask_price_EUR < ask_price_BTC):
     #   MSG_INFO[4] = '[4] ask_price_EUR < ask_price_BTC'
    #    INFO = '[4] Buy EUR and Hold BTC   '
        state.append('4')
    if (ask_price_EUR > ask_price_BTC):
      #  MSG_INFO[5] = '[5] ask_price_EUR > ask_price_BTC'
    #    INFO = '[5] Buy BTC and Hold EUR   '
        state.append('5')
    if (bid_price_EUR > bid_price_BTC):
       # MSG_INFO[2] = '[2] bid_price_EUR > bid_price_BTC'
    #    INFO = '[2] Sell EUR and Hold BTC  '
        state.append('2')

    if (bid_price_EUR < bid_price_BTC):
        #MSG_INFO[3] = '[3] bid_price_EUR < bid_price_BTC'
    #    INFO = '[3] Sell BTC and Hold EUR  '
        state.append('3')
    #else:
    #    INFO = 'Undefine State: '
    #MSG_INFO[6] = '[6] undefined state              '
    #    state.append('6')

    if '0' in state:
        if btc_naobtc >= 0:
            available_xlm_bid = float(bid_amount_BTC)/float(bid_price_BTC)
            if r_xlm_naobtc <= C_xlm_naobtc:
                possible_amount_to_buy = float(C_xlm_naobtc) - float(r_xlm_naobtc)
                if possible_amount_to_buy < available_xlm_bid:
                    real_amount_to_buy = possible_amount_to_buy
                else:
                    if available_xlm_bid <= C_max_trade_xlm:
                        real_amount_to_buy = available_xlm_bid
                    else:
                        real_amount_to_buy = C_max_trade_xlm

                r_xlm_naobtc = float(r_xlm_naobtc) + float(real_amount_to_buy)
                btc_naobtc =  float(btc_naobtc) - float(real_amount_to_buy)*float(bid_price_BTC)

        if r_xlm_tempo >= C_xlm_tempo:
            possible_amount_to_sell = float(r_xlm_tempo) - float(C_xlm_tempo)
            if possible_amount_to_sell < ask_amount_EUR:
                real_amount_to_sell = possible_amount_to_sell
            else:
                if ask_amount_EUR <= C_max_trade_xlm:
                    real_amount_to_sell = ask_amount_EUR
                else:
                    real_amount_to_sell = C_max_trade_xlm
            r_xlm_tempo = float(r_xlm_tempo) - real_amount_to_sell
            eur_tempo = float(eur_tempo) + float(real_amount_to_sell)*ask_price_EUR

        MSG_ACTION = '[0] Sell BTC '+str(float(real_amount_to_buy))+ '(xlm) and Buy EUR   '+ str(real_amount_to_sell)+'(xlm). Total XLM in naobtc:'+str(r_xlm_naobtc)+' Total XLM in Tempo:'+str(r_xlm_tempo) + ' Total Euro: ' +str(eur_tempo) + ' Total BTC:' +str(btc_naobtc)
        #print(MSG_INFO + MSG_ACTION)
        f.write("%s : %s %s \n"%(LOG_TIME,MSG_INFO['0'],MSG_ACTION))
    if '1' in state:
        if eur_tempo >= 0:
            available_xlm_bid = float(bid_amount_EUR)/float(bid_price_EUR)
            if r_xlm_tempo <= C_xlm_naobtc:
                possible_amount_to_buy = float(C_xlm_tempo) - float(r_xlm_tempo)
                if possible_amount_to_buy < available_xlm_bid:
                    real_amount_to_buy = possible_amount_to_buy
                else:
                    if available_xlm_bid <= C_max_trade_xlm:
                        real_amount_to_buy = available_xlm_bid
                    else:
                        real_amount_to_buy = C_max_trade_xlm

                r_xlm_tempo = float(r_xlm_tempo) + float(real_amount_to_buy)
                eur_tempo = eur_tempo - float(real_amount_to_buy)*float(bid_price_EUR)
        if r_xlm_naobtc >= C_xlm_naobtc:
            possible_amount_to_sell = float(r_xlm_naobtc) - float(C_xlm_naobtc)
            if possible_amount_to_sell < ask_amount_BTC:
                real_amount_to_sell = possible_amount_to_sell
            else:
                if ask_amount_BTC <= C_max_trade_xlm:
                    real_amount_to_sell = ask_amount_BTC
                else:
                    real_amount_to_sell = C_max_trade_xlm
            r_xlm_naobtc = float(r_xlm_naobtc) - real_amount_to_sell
            btc_naobtc = float(btc_naobtc)+float(real_amount_to_sell)*ask_price_BTC
        MSG_ACTION = '[1] Sell EUR '+str(float(real_amount_to_buy))+ '(xlm) and Buy BTC   '+ str(real_amount_to_sell)+'(xlm). Total XLM in naobtc:'+str(r_xlm_naobtc)+' Total XLM in Tempo:'+str(r_xlm_tempo) + ' Total Euro: ' +str(eur_tempo) + ' Total BTC:' +str(btc_naobtc)
        #print(MSG_INFO + MSG_ACTION)
        f.write("%s : %s %s \n"%(LOG_TIME,MSG_INFO['1'],MSG_ACTION))
    if '2' in state:
        if eur_tempo >= 0:
            available_xlm_bid = float(bid_amount_EUR)/float(bid_price_EUR)
            if r_xlm_tempo <= C_xlm_tempo:
                possible_amount_to_buy = float(C_xlm_tempo) - float(r_xlm_tempo)
                if possible_amount_to_buy < available_xlm_bid:
                    real_amount_to_buy = possible_amount_to_buy
                else:
                    if available_xlm_bid <= C_max_trade_xlm:
                        real_amount_to_buy = available_xlm_bid
                    else:
                        real_amount_to_buy = C_max_trade_xlm

                r_xlm_tempo = float(r_xlm_tempo) + float(real_amount_to_buy)
                eur_tempo = eur_tempo - float(real_amount_to_buy)*float(bid_price_EUR)

        MSG_ACTION = '[2] Sell EUR '+str(real_amount_to_buy)+ '(xlm) and HOLD BTC. Total XLM in naobtc:'+str(r_xlm_naobtc)+' Total XLM in Tempo:'+str(r_xlm_tempo) + ' Total Euro: ' +str(eur_tempo) + ' Total BTC:' +str(btc_naobtc)
        #print(MSG_INFO + MSG_ACTION)
        f.write("%s : %s %s \n"%(LOG_TIME,MSG_INFO['2'],MSG_ACTION))

    if '3' in state:
        if btc_naobtc >= 0:
            available_xlm_bid = float(bid_amount_BTC)/float(bid_price_BTC)
            if r_xlm_naobtc <= C_xlm_naobtc:
                possible_amount_to_buy = float(C_xlm_naobtc) - float(r_xlm_naobtc)
                if possible_amount_to_buy < available_xlm_bid:
                    real_amount_to_buy = possible_amount_to_buy
                else:
                    if available_xlm_bid <= C_max_trade_xlm:
                        real_amount_to_buy = available_xlm_bid
                    else:
                        real_amount_to_buy = C_max_trade_xlm
                r_xlm_naobtc = float(r_xlm_naobtc) + float(real_amount_to_buy)
                btc_naobtc =  float(btc_naobtc) - float(real_amount_to_buy)*float(bid_price_BTC)

        MSG_ACTION = '[3] Sell BTC '+str(float(real_amount_to_buy))+ '(xlm) and HOLD EUR. Total XLM in naobtc:'+str(r_xlm_naobtc)+' Total XLM in Tempo:'+str(r_xlm_tempo) + ' Total Euro: ' +str(eur_tempo) + ' Total BTC:' +str(btc_naobtc)
        #print(MSG_INFO + MSG_ACTION)
        f.write("%s : %s %s \n"%(LOG_TIME,MSG_INFO['3'],MSG_ACTION))
    if '4' in state:
        if r_xlm_tempo >= C_xlm_tempo:
            possible_amount_to_sell = float(r_xlm_tempo) - float(C_xlm_tempo)
            if possible_amount_to_sell < ask_amount_EUR:
                real_amount_to_sell = possible_amount_to_sell
            else:
                if ask_amount_EUR <= C_max_trade_xlm:
                    real_amount_to_sell = ask_amount_EUR
                else:
                    real_amount_to_sell = C_max_trade_xlm
            r_xlm_tempo = float(r_xlm_tempo) - real_amount_to_sell
            eur_tempo = float(eur_tempo) + float(real_amount_to_sell)*ask_price_EUR

        MSG_ACTION = '[4] Buy EUR '+str(float(real_amount_to_sell))+ '(xlm) and HOLD BTC. Total XLM in naobtc:'+str(r_xlm_naobtc)+' Total XLM in Tempo:'+str(r_xlm_tempo) + ' Total Euro: ' +str(eur_tempo) + ' Total BTC:' +str(btc_naobtc)
        #print(MSG_INFO + MSG_ACTION)
        f.write("%s : %s %s \n"%(LOG_TIME,MSG_INFO['4'],MSG_ACTION))
    if '5' in state:
        if r_xlm_naobtc >= C_xlm_naobtc:
            possible_amount_to_sell = float(r_xlm_naobtc) - float(C_xlm_naobtc)
            if possible_amount_to_sell < ask_amount_BTC:
                real_amount_to_sell = possible_amount_to_sell
            else:
                if ask_amount_BTC <= C_max_trade_xlm:
                    real_amount_to_sell = ask_amount_BTC
                else:
                    real_amount_to_sell = C_max_trade_xlm
            r_xlm_naobtc = float(r_xlm_naobtc) - real_amount_to_sell
            btc_naobtc = float(btc_naobtc)+float(real_amount_to_sell)*ask_price_BTC
        MSG_ACTION = '[5] Buy BTC '+str(float(real_amount_to_sell))+ '(xlm) and HOLD EUR. Total XLM in naobtc:'+str(r_xlm_naobtc)+' Total XLM in Tempo:'+str(r_xlm_tempo) + ' Total Euro: ' +str(eur_tempo) + ' Total BTC:' +str(btc_naobtc)
        #print(MSG_INFO + MSG_ACTION)
        f.write("%s : %s %s \n"%(LOG_TIME,MSG_INFO['5'],MSG_ACTION))
    if '6' in state:
        MSG_ACTION = '[6] Total XLM in naobtc:'+str(r_xlm_naobtc)+' Total XLM in Tempo:'+str(r_xlm_tempo) + ' Total Euro: ' +str(eur_tempo) + ' Total BTC:' +str(btc_naobtc)
        #print(MSG_INFO + MSG_ACTION)
        f.write("%s : %s %s \n"%(LOG_TIME,MSG_INFO['6'],MSG_ACTION))
    #f.write("%s \n"%(str(state)))
    pbar.update(running_times+1)
pbar.finish()
f.close()
