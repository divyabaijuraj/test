""""""""""""""""
def calculator(num1,num2,sign):
     print(num1,num2,sign)
     if(sign == "+"):
         return num1+num2


print("Enter the numbers and operation sign:")
num1=input()
num2=input()
sign=input()
calculator(num1,num2,sign)



"""




import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://indianredcross.org/ircs/donatenow")
driver.maximize_window()

action_obj = webdriver.ActionChains(driver)
first_name = driver.find_element(By.ID, 'edit-your-name-first')
last_name = driver.find_element(By.ID, 'edit-your-name-last')

action_obj.key_down(Keys.SHIFT).send_keys_to_element(first_name, "divya").perform()
time.sleep(1)
action_obj.context_click(first_name.perform)
last_name.send_keys("Divya")

action_obj.key_down(Keys.COMMAND).send_keys_to_element(last_name, "a").perform()
action_obj.double_click(last_name).perform()
time.sleep(10)
