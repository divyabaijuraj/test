import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(2)

depart_city = "Dallas Fort Worth"

# city = 'Udhagamandalam'
# search_field = driver.find_element(By.ID, "input-auto-complete")

depart = driver.find_element(By.ID, "BE_flight_origin_city")
depart.click()
time.sleep(2)

for x in depart_city:
    depart.send_keys(x)
depart.send_keys(Keys.ENTER)

time.sleep(4)

arrival_city = "Dubai"
arrival = driver.find_element(By.ID, "BE_flight_arrival_city")
arrival.click()

time.sleep(1)

for x in arrival_city:
    arrival.send_keys(x)
arrival.send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.ID, 'BE_flight_origin_date').click()

time.sleep(2)

# //div[@class="day-container"]//child::td

# //*[@class="datepicker flex1 activeBox"]//child::td
depart_date='09/02/2022'
calendar_dates = driver.find_elements(By.XPATH, '//*[@class="day-container"]//child::td')
#print(len(calendar_dates))

for date in calendar_dates:
   if(date.get_attribute("data-date") == depart_date):
       print("Correct date","&&&&&&")
       date.click()
       break

time.sleep(4)



driver.find_element(By.ID,"BE_flight_flsearch_btn").click()
time.sleep(3)
#book_now=driver.find_elements(By.XPATH,'//*[@class="fs-14 secondary-button button cursor-pointer bold"]')
book_now=driver.find_elements(By.XPATH,"//*[@class='full mb-8 fs-13 airline-name']")



print(len(book_now))
for flight in book_now:
    print(flight.text)
time.sleep(4)


