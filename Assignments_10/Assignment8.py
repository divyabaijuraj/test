#form-control js-site-search-input ui-autocomplete-input ui-autocomplete-loading
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.shoppersstop.com/")
driver.switch_to.alert.dismiss()
driver.maximize_window()
time.sleep(2)
search=driver.find_element(By.XPATH,"//input[@name='text']")

search.click()
search.send_keys('Tommy Hilfiger')
search.send_keys(Keys.ENTER)

belt=driver.find_elements(By.XPATH,"//div[@class='pro-info card-body col-md-12 col-sm-12 col-xs-12']//child::a//input[contains(@value,'belt')]")
time.sleep(10)
print(len(belt))


