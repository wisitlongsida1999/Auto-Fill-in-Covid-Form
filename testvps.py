from selenium import webdriver
import time
import requests
import datetime

url = 'https://notify-api.line.me/api/notify'
token = 'NueINfPN2wYyWK8eQ0pu221VumB8x1AghFYVVfBi8Iq'
headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}

list_holiday=['07/28/21','08/12/21','10/13/21','10/23/21','12/05/21','12/10/21','12/31/21']

now = datetime.datetime.now()
while(True):
    time.sleep(10)
    requests.post(url, headers=headers, data={'message': ">>> Fill in Complete !!!"}).text

