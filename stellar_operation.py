#createBidOffer(PrivateKey,'xml_eurt','0.0000000001','1')
#createAskOffer(PrivateKey,'xml_eurt','500','0.001')
#checkBalance('xlm') #btc,xlm,eurt

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import time

def createBidOffer(PrivateKey,Trading_Pair,price,amount):
    browser = webdriver.Chrome(executable_path=r'C:\Users\Ahaxin\PycharmProjects\chromedriver.exe')
    # Login
    browser.get('https://stellarterm.com/#account')
    private_key_input = browser.find_element_by_css_selector("input.s-inputGroup__item.S-flexItem-share.LoginPage__password")
    private_key_input.send_keys(PrivateKey)
    private_key_input.submit()
    time.sleep(0.1)
    if Trading_Pair == 'xml_eurt': #Buy XLM using EURT
        Market = 'https://stellarterm.com/#exchange/XLM-native/EURT-tempo.eu.com'
        price_xpath   = '//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/form/table/tbody/tr[1]/td[2]/label/input'
        amount_xpath  = '//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/form/table/tbody/tr[2]/td[2]/label/input'
        confirm_xpath = '//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/form/div/input'

    browser.get(Market)
    time.sleep(1)

    #Buy XLM using EURT
    price_input = browser.find_element_by_xpath(price_xpath)
    time.sleep(1)
    price_input.clear()
    price_input.send_keys(price)

    amount_input = browser.find_element_by_xpath(amount_xpath)
    amount_input.clear()
    amount_input.send_keys(amount)
    amount_input.send_keys(Keys.ENTER)
    time.sleep(0.1)
    confirm = browser.find_element_by_xpath(confirm_xpath)
    confirm.click()
    time.sleep(5)

def createAskOffer(PrivateKey,Trading_Pair,price,amount):
    browser = webdriver.Chrome(executable_path=r'C:\Users\Ahaxin\PycharmProjects\chromedriver.exe')
    # Login
    browser.get('https://stellarterm.com/#account')
    private_key_input = browser.find_element_by_css_selector("input.s-inputGroup__item.S-flexItem-share.LoginPage__password")
    private_key_input.send_keys(PrivateKey)
    private_key_input.submit()
    time.sleep(0.1)
    if Trading_Pair == 'xml_eurt': #Sell XLM for EURT
        Market = 'https://stellarterm.com/#exchange/XLM-native/EURT-tempo.eu.com'
        price_xpath   = '//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/form/table/tbody/tr[1]/td[2]/label/input'
        amount_xpath  = '//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/form/table/tbody/tr[2]/td[2]/label/input'
        confirm_xpath = '//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/form/div/input'

    browser.get(Market)
    time.sleep(1)

    price_input = browser.find_element_by_xpath(price_xpath)
    time.sleep(1)
    price_input.clear()
    price_input.send_keys(price)

    amount_input = browser.find_element_by_xpath(amount_xpath)
    amount_input.clear()
    amount_input.send_keys(amount)
    amount_input.send_keys(Keys.ENTER)
    time.sleep(0.1)
    confirm = browser.find_element_by_xpath(confirm_xpath)
    confirm.click()
    time.sleep(5)

def checkBalance(asset_code):
    url = 'https://horizon.stellar.org/accounts/GAHVZIKQ7OGNLPMYM75D6F6CUI6YQOJ2K5VXATNXLO5HPZHB64LFX7TS'
    response = requests.get(url)
    content = response.content.decode()
    balanceList = json.loads(content)['balances']
    balance = 0.0000000000
    asset_code = asset_code.upper()

    for items in balanceList:
        if 'asset_code' in items:
            if items['asset_code'] == asset_code:
                balance = float(balance) + float(items['balance'])
        else:
            if (items['asset_type'] == 'native') and asset_code == 'XLM':
                balance = float(items['balance'])
    return balance


