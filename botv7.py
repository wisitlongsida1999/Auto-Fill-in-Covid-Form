from selenium import webdriver
import time
import requests
import datetime
import random
import traceback


url = 'https://notify-api.line.me/api/notify'
token = 'Useey72VZw50pS3xgsH6iWMheGjbKTd44Tewgm85j6F'
headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}

list_holiday=['04/12/22','04/13/22','04/14/22','04/15/22','05/02/22','05/04/22','05/16/22','06/03/22','07/13/22','07/14/22','07/28/22','07/29/22','08/12/22','10/13/22','10/14/22','10/23/22','10/24/22','12/05/22','12/10/22','12/12/22','12/25/22','12/31/22']

r = 8


while (True):

    en = ''

    now = datetime.datetime.now()
    print(now)


    if((now.strftime("%A") == "Saturday" )or (now.strftime("%A") == "Sunday") or now.strftime("%D") in list_holiday):
        
        if ((now.hour == 0 and now.minute == r) or (now.hour == 10 and now.minute == r)):

            en = '512247'

        elif ((now.hour == 1 and now.minute == r) or (now.hour == 11 and now.minute == r)):

            en = '515286'


        if en:

            try:
                wd = webdriver.Chrome()
                wd.get("https://www.fabrinet.co.th/custappl/covid/")
                wd.find_element_by_xpath('//input[@type="text"]').send_keys(en)
                time.sleep(1)
                wd.find_element_by_xpath('//input[@type="submit"]').click()
                time.sleep(5)
                wd.find_elements_by_xpath('//span[@id="workat"]')[3].click()
                time.sleep(1)
                wd.find_elements_by_xpath('//span[@class="checkmark"]')[14].click()
                time.sleep(1)
                wd.find_element_by_xpath('//span[@id="checkbox13"]').click()
                time.sleep(1)
                wd.find_element_by_xpath('//span[@id="checkbox14"]').click()
                time.sleep(1)
                wd.find_element_by_xpath('//input[@type="submit"]').click()
                time.sleep(1)
                wd.quit()
                r = random.randint(1, 30)
                print("Complete")
                requests.post(url, headers=headers, data={'message': f" EN: {en} >>> Fill in Complete !!!  @"+str(now)}).text

            except:
                print("Error")
                requests.post(url, headers=headers, data={'message': f" EN: {en} >>> Fill in Failed !!!  @"+str(now)}).text

            time.sleep(60*30)


    else:
        if ((now.hour == 0 and now.minute == r) or (now.hour == 10 and now.minute == r)):

            en = '512247'

        elif ((now.hour == 1 and now.minute == r) or (now.hour == 11 and now.minute == r)):

            en = '515286'


        if en :

            try:
                wd = webdriver.Chrome()
                wd.get("https://www.fabrinet.co.th/custappl/covid/")
                wd.find_element_by_xpath('//input[@type="text"]').send_keys(en)
                time.sleep(1)
                wd.find_element_by_xpath('//input[@type="submit"]').click()
                time.sleep(5)
                wd.find_elements_by_xpath('//span[@id="workat"]')[0].click()
                time.sleep(1)
                wd.find_elements_by_xpath('//span[@class="checkmark"]')[14].click()
                time.sleep(1)
                wd.find_element_by_xpath('//span[@id="checkbox13"]').click()
                time.sleep(1)
                wd.find_element_by_xpath('//span[@id="checkbox14"]').click()
                time.sleep(1)
                wd.find_element_by_xpath('//input[@type="submit"]').click()
                time.sleep(1)
                wd.quit()
                r = random.randint(1, 30)
                print("Complete")
                requests.post(url, headers=headers, data={'message': f" EN: {en} >>> Fill in Complete !!!  @"+str(now)}).text

            except:
                print("Error")
                requests.post(url, headers=headers, data={'message': f" EN: {en} >>> Fill in Failed !!!  @"+str(now)}).text

            time.sleep(60*30)

    time.sleep(30)

    