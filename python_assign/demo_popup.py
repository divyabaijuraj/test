import time

from select import select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
##Launch salesforce url
driver.get("https://www.softwaretestinghelp.com/handle-alerts-popups-selenium-webdriver-selenium-tutorial-16/")
# driver.get("https://www.yatra.com/")

driver.maximize_window()

time.sleep(20)
#driver.switch_to.alert.dismiss()

time.sleep(4)