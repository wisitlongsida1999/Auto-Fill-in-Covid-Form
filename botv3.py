from selenium import webdriver
import time
import requests
import datetime
import random


url = 'https://notify-api.line.me/api/notify'
token = 'NueINfPN2wYyWK8eQ0pu221VumB8x1AghFYVVfBi8Iq'
headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}

list_holiday=['07/28/21','08/12/21','10/13/21','10/23/21','12/05/21','12/10/21','12/31/21']

r = 30


while (True):

    now = datetime.datetime.now()
    print(now)



    if((now.strftime("%A") == "Saturday" )or (now.strftime("%A") == "Sunday") or now.strftime("%D") in list_holiday):
        if ((now.hour == 17 and now.minute == r) or (now.hour == 10 and now.minute == r)):

            try:
                wd = webdriver.Chrome()
                wd.get("https://www.fabrinet.co.th/custappl/covid/")
                wd.find_element_by_xpath('//input[@type="text"]').send_keys('512247')
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
                r = random.randint(0, 30)
                print("Complete")
                requests.post(url, headers=headers, data={'message': ">>> Fill in Complete !!!  @"+str(now)}).text

            except:
                print("Error")
                requests.post(url, headers=headers, data={'message': ">>> Fill in Failed !!!  @"+str(now)}).text

            time.sleep(60*30)


    else:
        if ((now.hour == 22 and now.minute == r) or (now.hour == 10 and now.minute == r)):

            try:
                wd = webdriver.Chrome()
                wd.get("https://www.fabrinet.co.th/custappl/covid/")
                wd.find_element_by_xpath('//input[@type="text"]').send_keys('512247')
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
                r = random.randint(0, 30)
                print("Complete")
                requests.post(url, headers=headers, data={'message': ">>> Fill in Complete !!!  @"+str(now)}).text

            except:
                print("Error")
                requests.post(url, headers=headers, data={'message': ">>> Fill in Failed !!!  @"+str(now)}).text

            time.sleep(60*30)

    time.sleep(30)

