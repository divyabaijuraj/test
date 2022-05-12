import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
##Launch salesforce url
driver.get("https://www.salesforce.com/in/")
driver.maximize_window()
time.sleep(2)
##click on resource tab

resource=driver.find_element(By.ID,"solutions_menu_item")
previous_url=driver.current_url
resource.click()
driver.implicitly_wait(3)
##Select the blog from resource menu through XPATH

driver.find_element(By.XPATH, '//*[@id="drawer_solutions"]/div/div/div[1]/ul/li/div/ul/li[1]/a').click()
current_url=driver.current_url

if(current_url == previous_url):
    print("Both the windows contain same company url")
time.sleep(10)
#view demo
list1=driver.find_elements(By.XPATH, "/html/body/div[3]/div/div/div/div/div[1]/div[1]/div/nav/ul/li/child::a")
print(list1)

#//*[@id="view-demo_menu_item"]
#/html/body/div[3]/div/div
time.sleep(4)