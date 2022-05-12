
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://editorial.rottentomatoes.com/guide/best-netflix-shows-and-movies-to-binge-watch-now/")
driver.maximize_window()
time.sleep(2)
#ranks=driver.find_elements(By.XPATH,"//div[@class='col-sm-4 col-full-xs']//child::div[@class='countdown-index']")
ranks=driver.find_elements(By.XPATH,"//div[@class='articleContentBody']//div[@class='row countdown-item']")

str1=""
for rank in ranks:
  str1= str1+rank.text
result=str1.find('#108')
if(result != -1)   :
  details = driver.find_elements(By.XPATH, "//*[@id = 'row-index-108']/div[2]/div[2]/div/div[2]")
  for x in details:
    print(x.text)
