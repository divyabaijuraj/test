from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

for element in driver.find_elements(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/footer[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/p[2]'):
   #print(element.text)
    str=element.text
   # print(str.index('Fax'))
   # print(str.find('Fax'))
    print("Fax ",str[30:56])




