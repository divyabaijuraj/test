import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#Launch the website
driver.get("https://www.india.gov.in/")
driver.maximize_window()
#click the calendar link

driver.find_element(By.XPATH,"//*[@id='home']/div/div/div[5]/div/div/div/ul/li[3]/a").click()
time.sleep(4)
#Navigate to the next month (March)by clicking next button
driver.find_element(By.XPATH,"//*[@id='block-system-main']/div/div[1]/div/div/ul/li[2]/a").click()
time.sleep(4)

#To get the number of holidays
dates=driver.find_elements(By.XPATH,"//table[@class='full']//child::div[@title='Key: Holiday Calendar']")
number_of_holidays =(len(dates))
print("Number of holidays: ",number_of_holidays)

#To print the names of holidays
holidays=driver.find_elements(By.XPATH,"//table[@class='full']//child::span[@class='field-content']")
for days in holidays:
      print(days.text)