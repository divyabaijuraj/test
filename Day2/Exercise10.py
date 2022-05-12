import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9")
driver.maximize_window()
time.sleep(2)


banks=driver.find_elements(By.XPATH,'//*[@id="mc_mainWrapper"]/div[2]/div[1]/div[5]/div[2]/div/table/tbody/tr/td')
print(len(banks))
c=0
for i in banks:

    if(i.text=="Axis Bank"):
        while(c<=6):
                print(i.text)
                c=c+1
        break


