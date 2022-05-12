#//div[@class='container scroll_section_data_sotc']//child::div[@class='owl-stage']
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import re

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


##Launch  url
driver.get("https://www.sotc.in/")
driver.maximize_window()
time.sleep(3)
#dest=driver.find_elements(By.XPATH,"//div[@class='container scroll_section_data_sotc']//child::div[@class='owl-stage']")
dest=driver.find_elements(By.XPATH,"//*[@class='owl-item active']//child::*[@class='trending_price_slide']")
print(len(dest))
str1=''
for x in dest:
    print(x.text)

"""
str1=''
str2=''

for x in dest:
    str1+=x.text
#Replace the special characters from a string
#print(str1)
str1 = str1.replace("₹", " ")
str1 = str1.replace("/-", " ")
str2=str1
#Remove all the white spaces from string
str1 = re.sub(r'(\d)\s+(\d)', r'\1\2', str1)
#get the list of prices of packages in a page
#print([int(price) for price in str1.split() if price.isdigit()])

#max of the prices
maxprice=(max([int(price) for price in str1.split() if price.isdigit()]))
#print(maxprice)
time.sleep(4)


for x in dest:
    print(x.text.replace(" ",""))
    if str(maxprice) in (x.text.replace(" ","")):

        x.click()
        break
time.sleep(4)


"""