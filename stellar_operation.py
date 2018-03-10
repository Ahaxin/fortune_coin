from selenium import webdriver
browser = webdriver.Chrome(executable_path=r'C:\Users\Ahaxin\PycharmProjects\chromedriver.exe')
browser.get('https://stellarterm.com/#account')
private_key_input = browser.find_element_by_css_selector("input.s-inputGroup__item.S-flexItem-share.LoginPage__password")

private_key_input.send_keys('')

private_key_input.submit()

XLM_EURT = 'https://stellarterm.com/#exchange/XLM-native/EURT-tempo.eu.com'

browser.get(XLM_EURT)


#from robobrowser import RoboBrowser
#browser = RoboBrowser()
#login_url = 'https://stellarterm.com/#account'
#browser.open(login_url)
#form = browser.get_form(class_='s-inputGroup__item S-flexItem-share LoginPage__password')
#print(form)
#form['value'].value = 1
#browser.submit_form(form)

import bs4
from robobrowser import RoboBrowser

#Check Balance
# https://horizon.stellar.org/accounts/GAHVZIKQ7OGNLPMYM75D6F6CUI6YQOJ2K5VXATNXLO5HPZHB64LFX7TS   Native is XLM

#<input type="password" class="s-inputGroup__item S-flexItem-share LoginPage__password" value="" placeholder="Secret key (example: SBSMVCIWBL3HDB7N4EI3QKBKI4D5ZDSSDF7TMPB.....)">



#log_in_form = browser.get_form(class_='s-inputGroup__item S-flexItem-share LoginPage__password')

#print(log_in_form)
#log_in_form['value']
#<input type="password" class="s-inputGroup__item S-flexItem-share LoginPage__password" value="" placeholder="Secret key (example: SBSMVCIWBL3HDB7N4EI3QKBKI4D5ZDSSDF7TMPB.....)">

