import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Launch URL "http://trivago.in"
driver.get("https://trivago.in")
driver.maximize_window()

#Search trivago_price_filter.pyand select from result for city 'Udhagamandalam'
time.sleep(2)
city = 'Udhagamandalam'
search_field = driver.find_element(By.ID, "input-auto-complete")

for x in city:
    search_field.send_keys(x)

time.sleep(2)
search_field.send_keys(Keys.ENTER)
time.sleep(2)

#Check in date as '2022-02-20'
check_in_date = '2022-02-20'

calendar_ele = driver.find_elements(By.XPATH, '//*[@class="DatePicker_calendarMonth__k1Al4"]//child::time')
for x in calendar_ele:
    date_time = x.get_attribute("datetime")
    print(date_time)
    print(check_in_date)
    if date_time == check_in_date:
        x.click()
time.sleep(1)

#Check out date as '2022-02-27'
check_out_date = '2022-02-27'
for x in calendar_ele:
    print(x.text)
    date_time_out=x.get_attribute("datetime")
    if date_time_out == check_out_date:
        x.click()
        break

time.sleep(2)

#Click on serach button
search_btn = driver.find_element(By.XPATH, "//span[@class='w-full text-center font-bold']")
search_btn.click()

time.sleep(5)

#In the search result page, close the map

driver.find_element(By.XPATH, "//*[@class='inline-flex leading-none transform']").click()



#Filter the 'Sort By' filed by "Price Only"
time.sleep(5)
sort_by = driver.find_element(By.XPATH, "//div[@class='flex items-center']//child::select")
select_obj = Select(sort_by)
time.sleep(1)
select_obj.select_by_visible_text("Price only")

time.sleep(10)

#Validate the prices, it's expected to be in increasing order

rec_price = driver.find_elements(By.XPATH, "//p[@data-testid='recommended-price']")

price_list = []
for x in rec_price:
    print(x.text)
    price_list.append(x.text)

int_list = []
print(price_list)
for x in price_list:
    print(int(x [1:]))
    int_list.append(int(x [1:]))

result_sort = sorted(int_list)
if int_list == result_sort:
    print("Sorted")

