import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Launch URL "http://trivago.in"
driver.get("https://trivago.in")
driver.maximize_window()

#Search and select from result for city 'Udhagamandalam'
time.sleep(2)
city = 'Udhagamandalam'
search_field = driver.find_element(By.ID, "input-auto-complete")

for x in city:
    search_field.send_keys(x)

time.sleep(2)
search_field.send_keys(Keys.ENTER)
time.sleep(2)

#Check in date as '2022-02-20'
check_in_date = '2022-02-20'

calendar_ele = driver.find_elements(By.XPATH, '//*[@class="DatePicker_calendarMonth__k1Al4"]//child::time')
print(calendar_ele)
for x in calendar_ele:
    # print(x.text)
    print(x.get_attribute("datetime"))
    if x.get_attribute("datetime") == check_in_date:
        x.click()
        break

time.sleep(1)

#Check out date as '2022-02-27'
check_out_date = '2022-02-27'
for x in calendar_ele:
    # print(x.text)
    # print(x.get_attribute("datetime"))
    if x.get_attribute("datetime") == check_out_date:
        x.click()
        break
