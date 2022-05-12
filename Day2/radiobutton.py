
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
import time
driver.get("https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")
time.sleep(20)


driver.find_element(By.XPATH,'//*[@id="align"]/span[4]/input').click()

