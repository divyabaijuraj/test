import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.action_chains import ActionChains
#Launch “https://www.hdfcbank.com/personal/tools-and-calculators"
driver.get("https://www.hdfcbank.com/personal/tools-and-calculators")
driver.maximize_window()
time.sleep(2)
#close the pop up frame
driver.find_element(By.ID, "nvpush_cross").click()
driver.find_element(By.XPATH,'//div[@id="onetrust-button-group"]//child::button[@id="onetrust-accept-btn-handler"]').click()
time.sleep(2)

# click on loans
loans=driver.find_element(By.XPATH,"//*[@id='main']/div[2]/div[12]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[1]/div[1]/div[2]").click()
time.sleep(2)
# car loan EMI calculator   " + " icon
#driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[12]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]').click()

#  Car Loan EMI calculator '+' icon

carplus_btn=driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[12]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/h3')
carplus_btn.click()
time.sleep(2)

# Click on the button "CALCULATE NOW"

calculate_btn=driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[12]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/a')
calculate_btn.click()
time.sleep(2)
#“Amount of" - 1000000, "Years" - 5 yrs, "Interest rate" - 10%
action = webdriver.ActionChains(driver)
amount_box = '1000000'
search_amount=driver.find_element(By.XPATH,'//div[@class="rowbtc row mT20"]//child::input[@id="amt"]')
search_amount.click()
action.key_down(Keys.CONTROL).send_keys_to_element(search_amount, "a").perform()
time.sleep(2)
search_amount.send_keys(Keys.ESCAPE)
for i in amount_box:
    search_amount.send_keys(i)
time.sleep(2)


years_box='5'
search_years= driver.find_element(By.XPATH,'//div[@class="rowbtc row mT20"]//child::input[@id="years"]')
search_years.click()
action.key_down(Keys.CONTROL).send_keys_to_element(search_years, "a").perform()
search_years.send_keys(Keys.ESCAPE)
for j in years_box:
    search_years.send_keys(j)
time.sleep(2)

interest_box='10'
search_interest= driver.find_element(By.XPATH,'//div[@class="rowbtc row mT20"]//child::input[@id="int"]')
search_years.click()
action.key_down(Keys.CONTROL).send_keys_to_element(search_interest, "a").perform()
search_interest.send_keys(Keys.ESCAPE)
for k in interest_box:
    search_interest.send_keys(k)
time.sleep(2)

print(f"THE Given Amount is : ₹{amount_box}")
print(f"THE Given Duration is : {years_box} Years")
print(f"THE Given Rate Of Interest is : {interest_box}% ")
time.sleep(2)


# Step 6- Get the EMI value : “Your Monthly EMI will be ****** per month

calculate_box= driver.find_element(By.XPATH,'//a[@class="btcbt btn btcbt btn-primary "]')
calculate_box.click()
time.sleep(2)

monthly_emi=driver.find_element(By.XPATH,'//div[@class="rowbtc row mT20"]//child::span[@class="emiamt ng-binding"]')
print(f"The Monthly EMI will be: {monthly_emi.text} ")
time.sleep(2)
