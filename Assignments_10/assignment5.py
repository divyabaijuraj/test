import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://karnataka.gov.in/english")
driver.maximize_window()
time.sleep(2)
#Fetch the name of Hon'ble Governor of Karnataka
name=driver.find_element(By.XPATH,'//div[@class="sidebar-widgets profile-div visible-md visible-lg"]//child::h4')
print("Hon'ble Governor of Karnataka: ",name.text)
#Fetch the name of CM
cm=driver.find_element(By.XPATH,"//div[@class='sidebar-widgets visible-md visible-lg']//child::h4")
print("Chief Minister of Karnataka: ",cm.text)
#Select the Government menu
driver.find_element(By.XPATH,'//*[@id="na1"]/li[3]/a').click()
time.sleep(2)
#Select the Departments from Goverment menu
driver.find_element(By.XPATH,'//*[@id="na1"]/li[3]/ul/li[1]/a').click()

time.sleep(4)
departments=driver.find_elements(By.XPATH,"//ul[@class='nav nav-tabs tabs-left scroll3']//child::li")
#print(departments.text)
deptsort=[]
dept_list=[]
for dept in departments:
    str=dept.text
    dept_list=str.split('.')
    deptsort.append(dept_list[1])
#print(deptsort)

deptlist=[]
for i in deptsort:
     deptnames=i.replace('DEPARTMENT OF ','')
     deptlist.append(deptnames)
     sortlist_copy=deptlist[:]
print(deptlist)
sortlist_copy.sort()
print(sortlist_copy)
if(deptlist == sortlist_copy):
    print("Sorted")
else:
    print("Not sorted")