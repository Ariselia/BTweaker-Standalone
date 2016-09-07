import requests
import time

username = input('Please enter your username.\n')
password = input('Please enter your password.\n')
print('Logging in...')

s = requests.Session()
loginPayload = {'username': username, 'password': password, 'openid': ''}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
login = s.post("http://xnmn.v112.10000net.cn/login.do", data=loginPayload, headers=header)
# print(login.url)

getBalancePayload = {'addorsub': 'add', 'num': '0'}
rawCoinBalance = s.get("http://xnmn.v112.10000net.cn/coins.do", params=getBalancePayload, headers=header)
# print(rawCoinBalance.text)
coinBalance = int(rawCoinBalance.text)

if coinBalance < 0:
    print('Minus coin balance detected, fixing it.')
    addCoinNum = abs(coinBalance)
    addCoinPayload = {'addorsub': 'add', 'num': addCoinNum}
    addCoin = s.get("http://xnmn.v112.10000net.cn/coins.do", params=addCoinPayload, headers=header)
    print('All done, have fun!')
else:
    print('Your account status is OK, BTweaker is exiting now.')
    time.sleep(10)
