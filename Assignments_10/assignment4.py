import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.visualcapitalist.com/ranking-the-top-100-websites-in-the-world/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="tablepress-574_next"]').click()

time.sleep(4)

#2- Find the website which is on 19th rank

#website=driver.find_element(By.XPATH,'//table[@id="tablepress-574"]//child::tr[@class="row-20 even"]')
website=driver.find_element(By.XPATH,'//table[@id="tablepress-574"]//child::tr[@class="row-20 even"]//child::td[2]')
str1=website.text
print("Name of the website which has got 19th rank: ",str1)
#Fetch the name of country of above website
country_name=driver.find_element(By.XPATH,'//table[@id="tablepress-574"]//child::tr[@class="row-20 even"]//child::td[5]')
print("Name of the country: ",country_name.text)


