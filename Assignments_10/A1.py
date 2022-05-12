
"""
a='Hello'
b='I say Hello to you'
if a in b:
    print(f"{a} is present in the string: '{b}' .")


import string
#returns all uppercase letters
print(" ".join(string.ascii_uppercase))
#for ch in string.ascii_uppercase:
 #    print(ch,end=" ")

j=0
for i in range(10,16):
    for j in range(0,j+1):
        print(i,end=" ")

        j=j+1

"""

import time
# import action as action
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 1- Launch “https://www.hdfcbank.com/personal/tools-and-calculators"

driver.get("https://www.hdfcbank.com/personal/tools-and-calculators")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"nvpush_cross").click()
driver.find_element(By.XPATH,'//div[@id="onetrust-button-group"]//child::button[@id="onetrust-accept-btn-handler"]').click()
time.sleep(2)

# Step 2- Click on Loans

loan_btn=driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[12]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]')
loan_btn.click()
time.sleep(2)

# Step 3- Car Loan EMI calculator '+' icon

car_btn=driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[12]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/h3')
car_btn.click()
time.sleep(2)

# Step 4- Click on "CALCULATE NOW"

cal_btn=driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[12]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/a')
cal_btn.click()
time.sleep(2)

# Step 5- “Amount you need” - 1000000, Years - 5 yrs, Interest rate - 10%
action = webdriver.ActionChains(driver)

amount_box = '1000000'
search_amount=driver.find_element(By.XPATH,'//div[@class="rowbtc row mT20"]//child::input[@id="amt"]')
search_amount.click()
action.key_down(Keys.CONTROL).send_keys_to_element(search_amount, "a").perform()
time.sleep(2)
search_amount.send_keys(Keys.ESCAPE)
for i in amount_box:
    search_amount.send_keys(i)
time.sleep(2)

years_box='5'
search_years= driver.find_element(By.XPATH,'//div[@class="rowbtc row mT20"]//child::input[@id="years"]')
search_years.click()
action.key_down(Keys.CONTROL).send_keys_to_element(search_years, "a").perform()
search_years.send_keys(Keys.ESCAPE)
for j in years_box:
    search_years.send_keys(j)
time.sleep(2)

interest_box='10'
search_interest= driver.find_element(By.XPATH,'//div[@class="rowbtc row mT20"]//child::input[@id="int"]')
search_years.click()
action.key_down(Keys.CONTROL).send_keys_to_element(search_interest, "a").perform()
search_interest.send_keys(Keys.ESCAPE)
for k in interest_box:
    search_interest.send_keys(k)
time.sleep(2)

print("THE TYPED AMOUNT IS :", amount_box,'RUPEES')
print("THE TYPED YEAR IS :", years_box,'YEARS')
print("THE TYPED RATE OF INTEREST IS :", interest_box,'%')
time.sleep(2)

# Step 6- Get the EMI value : “Your Monthly EMI will be ****** per month

calculate_box= driver.find_element(By.XPATH,'//a[@class="btcbt btn btcbt btn-primary "]')
calculate_box.click()
time.sleep(2)
month_emi=driver.find_element(By.XPATH,'//div[@class="rowbtc row mT20"]//child::span[@class="emiamt ng-binding"]')
print('The monthly EMI will be ',month_emi.text,'per month')
time.sleep(2)

