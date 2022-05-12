import requests
import json
response=requests.get("https://api.covid19api.com/summary").json()
#print(response)
# data=json.load(response)
# print(data)
print(response)
"""

import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
##Launch salesforce url
driver.get("https://www.salesforce.com/in/form/demo/overview-demo/?nc=7010M0000022CzGQAU&d=7010M0000022CzLQAU")
driver.maximize_window()
time.sleep(2)
dropdwn=driver.find_element(By.NAME,"CompanyEmployees")
dd=Select(dropdwn)
dd.select_by_index(1)
time.sleep(2)
dd.select_by_visible_text("15 - 100 employees")
time.sleep(2)
dd.select_by_value("250")
time.sleep(3)
"""