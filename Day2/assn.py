"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://indianredcross.org/ircs/donatenow")

driver.maximize_window()
time.sleep(1)
parent_ele = driver.find_element(By.XPATH, '//*[@id="block-ircsnationalheadquarters"]//child::p[2]')
txt = parent_ele.get_attribute("innerHTML")
print(txt)
print(txt.split("Fax:")[1].split("<br>")[0])
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.fedex.com/en-us/about.html")

driver.maximize_window()
time.sleep(1)
parent_ele = driver.find_elements(By.XPATH, "//ul[@class='dropdown-menu']//child::li")
for x in parent_ele:
    print(x.get_attribute("innerHTML").split(">")[1].split("<")[0])