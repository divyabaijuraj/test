import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://icapability.ibridge360.com/")
driver.maximize_window()
time.sleep(2)

# btn = driver.find_element(By.CLASS_NAME, 'btn-2 btn btn-primary ')
# btn.click()

driver.find_element(By.XPATH,'//*[@id="root"]/div/nav/div/div[2]/div/a').click()
time.sleep(5)

# for email text box

eml = driver.find_element(By.XPATH, "//input[@placeholder = 'Enter Email']")
eml.click()
time.sleep(2)

usrid = "subhashkmr16@gmail.com"

for i in usrid:
    eml.send_keys(i)
time.sleep(1)
# eml.send_keys(Keys.ENTER)

time.sleep(2)

pswd = driver.find_element(By.XPATH, "//input[@placeholder = 'Enter Password']")
pswd.click()
password = 'aroha9065'

for i in password:
    pswd.send_keys(i)
time.sleep(1)
pswd.send_keys(Keys.ENTER)
time.sleep(2)

# login_btn = driver.find_element(By.CLASS_NAME, 'btn btn-primary login-button')
# login_btn.click()

result_btn = driver.find_element(By.XPATH,"//a[@href='/menu/UserResults']")
result_btn.click()
time.sleep(2)

driver.find_element(By.XPATH,"//tr[@id='MUIDataTableBodyRow-0']").click()
time.sleep(5)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(2)

corret_txt = driver.find_elements(By.XPATH,"//span[@style='color: green; float: right;']//child::b")
crt_ans= 0
for i in corret_txt:
    # print(i.text)
    crt_ans=crt_ans+1

time.sleep(3)
wrng_txt = driver.find_elements(By.XPATH,"//span[@style='color: red; float: right;']//child::b")
wrng_ans = 0
for i in wrng_txt:
    wrng_ans = wrng_ans+1
att = driver.find_elements(By.XPATH,"//span[@style='color: red;']")
nt_att = 0
for i in att:
    # print(i.text)
    if i.text == 'Not attempted':
        nt_att = nt_att+1

print("Total number of correct ans are : ", crt_ans)
print("Total number of wrong ans are : ", wrng_ans-nt_att)
print("Total number of not attempt questions are : ", nt_att)

time.sleep(10)

driver.switch_to_alert()
