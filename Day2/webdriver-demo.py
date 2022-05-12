from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(executable_path="\\Users\\Dell\\Desktop\\Browser\\chromedriver")

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.salesforce.com/in/?ir=1")

class_list=driver.find_elements(By.CLASS_NAME,"li-wrap")
print(len(class_list))
#a_list=driver.find_elements(By.TAG_NAME,"a")

#a_list=driver.find_elements(By.XPATH,"//*[@id='block-bartik-content']/div/article/div/div/table[1]/tbody/tr/td[1]/p[2]/strong/big/a")
a_list=driver.find_elements(By.XPATH,"//*[@href]")
a_len=len(a_list)
print(a_len)

y=0
for x in a_list:
    if x.text != "":
        print(x.text)
        y=y+1
print(y,"****************")

"""
driver.find_element(By.LINK_TEXT,"Product pricing").click()

#driver.find_element(Xpath,"//*[@id="block-ircsnationalheadquarters"]/div/div/p[2]/text()[2]")

#driver.get("https://indianredcross.org/ircs/")
"""
#######################
##Write a programme to find all the links in website - "https://indianredcross.org/ircs/"
a_list1=driver.find_elements(By.XPATH,"//a[@href]")
for item in a_list1:
    href=item.get_attribute("href")
    if href is not None:
        print(href)