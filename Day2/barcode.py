import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.barcodelookup.com/")
driver.maximize_window()
time.sleep(2)
search_string="CN-017BXW-76530-18S-1A3D"

driver.find_elements (By.XPATH,"//*[@class='search-bar']").send_keys("test")

time.sleep(3)



