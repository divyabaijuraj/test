import time

from select import select
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
print(current_url)

##Checking the current tab url matching with previous tab url

if(current_url == previous_url):
    print("Both tabs contain same company url")

time.sleep(10)
#view demo
#obtain parent window
if len(driver.window_handles) >0:
   first_window = driver.window_handles[0]

    #obtain browser tab window
   second_window = driver.window_handles[1]
   #switch to browser tab
   driver.switch_to.window(second_window)

   print("Page title for browser tab:")
   print(driver.title)
   #viewdemo


   driver.find_element(By.XPATH, "//*[@id='view-demo_menu_item']/a").click()
   time.sleep(3)
   print(len(driver.window_handles))
   print(driver.current_url)
   firstname=driver.find_element(By.XPATH, "//input[@name='UserFirstName']")
   firstname.click()
   firstname.send_keys("Divya")
   lastname=driver.find_element(By.XPATH, "//input[@name='UserLastName']")
   lastname.click()
   lastname.send_keys("Baijuraj")
   jobtitle=driver.find_element(By.XPATH,"//select[@name='UserTitle']//child::option[6]")
   jobtitle.click()
   email=driver.find_element(By.XPATH,"//input[ @ name = 'UserEmail']")
   email.click()
   email.send_keys("abc@gmail.com")

   phone=driver.find_element(By.XPATH,"//input[@name='UserPhone']")
   phone.click()
   phone.send_keys("9845656744")

   company=driver.find_element(By.XPATH, "//input[@name = 'CompanyName']")
   company.click()
   company.send_keys("abc technologies")

   employees=(driver.find_elements(By.XPATH,"//select[@name='CompanyEmployees']//child::option"))

  # print(employees)
   empnum='15 - 100 employees'
   for empno in employees:

      if(empno.text == empnum):
          empno.click()
          break

   country= driver.find_element(By.XPATH,"//select[@name='CompanyCountry']//child::option[99]")
   country.click()
   watchnow=driver.find_element(By.XPATH,'//div[@class="form_submit_button submitButton buttonCTAItemComponent parbase"]//child::button')
   watchnow.click()
   lnks = driver.find_elements(By.TAG_NAME,"a")
   print(len(lnks))
   # traverse list
   for lnk in lnks:
      # get_attribute() to get all href
      print(lnk.get_attribute('href'))
   time.sleep(20)






