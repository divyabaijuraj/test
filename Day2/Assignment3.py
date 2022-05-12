#Write a programme to find all the links in website - "https://indianredcross.org/ircs/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://indianredcross.org/ircs/")
a_list1=driver.find_elements(By.TAG_NAME,"a")
a_len1=len(a_list1)
print(a_len1)

y=0
for i in a_list1:
    if(i.text !=""):
        print(i.text)
        y=y+1
print(y)