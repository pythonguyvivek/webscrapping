from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.moneycontrol.com/')

main_page = BeautifulSoup(page.content, 'html.parser')
# Finding Class Containing Nifty50 Data

data_nifty50 = main_page.find_all(id="cp")
data_change = main_page.find_all(id="chg")
data_per_change = main_page.find_all(id="percentchange")
nifty50 = data_nifty50[0].get_text()
nifty50_change = data_change[0].get_text()
nifty50_per_change = data_per_change[0].get_text()

# Demostrtion
print("\t\t Nifty50 Data From MoneyControl")
print("\t Price:", nifty50)
print("\t Change:", nifty50_change)
print("\t % Change:", nifty50_per_change)
input()
