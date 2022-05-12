import xcelutilities
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://newtours.demoaut.com")
driver.maximize_window()
path="C:\\Users\\Dell\\Desktop\\login.xlsx"
rows=xcelutilities.getRowCount(path,'S1')
print(rows)
for r in range(0,rows):
    username=xcelutilities.readData(path,"S1",r,1)
    password=xcelutilities.readData(path,"S1",r,2)

    driver.find_element(By.Name,"userName").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.NAME,"login").click()
    if driver.titile == "Find a Flight:Mercury Tours":
        print("test is passed")
        xcelutilities.writeData(path,'S1',r,3,"test is passed")
    else:
        print("test failed")
        xcelutilities.writeData(path,'S1',r,3,"test is failed")


