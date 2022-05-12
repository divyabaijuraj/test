import time

from select import select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
##Launch scandidate url
driver.get("https://scandidate.in/#/login")
driver.maximize_window()
time.sleep(2)
#Enter the username ,password for login page
username=driver.find_element(By.XPATH,"//*[@id='mat-input-0']")
username.click()
username.send_keys("suraj.narayan@aroha.co.in")

time.sleep(2)
password=driver.find_element(By.XPATH,"//*[@id='mat-input-1']")
password.click()
password.send_keys("9036743392")
time.sleep(2)
#Click on the submit button in the login page
submit=driver.find_element(By.XPATH,"/html/body/app-root/app-login/div/div/div/div[2]/form/div[4]/button").click()
time.sleep(3)


##Navigate to the dashboard

dashboard=driver.find_element(By.XPATH,"/html/body/app-root/app-dashboard/app-navbar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/button").click()
#print(len(driver.window_handles))
time.sleep(4)

#Click on the operation Users
operation=driver.find_element(By.XPATH,"/html/body/app-root/app-dashboard/app-navbar/mat-sidenav-container/mat-sidenav/div/mat-nav-list/a[2]/div").click()
time.sleep(2)
#For Update on a user (Lakshmi mam) click on the edit
edit=driver.find_element(By.XPATH,"/html/body/app-root/app-organization-users-list/app-navbar/mat-sidenav-container/mat-sidenav-content/div/div[2]/table/tbody/mat-row[4]/mat-cell[7]/a/mat-icon/span")
edit.click()
#For updating the work location
worklocation = driver.find_element(By.XPATH, '//input[starts-with(@id,"mat-input-") and @formcontrolname="workstation"]')

# print(worklocation.text)

worklocation.click()
worklocation.clear()
worklocation.send_keys("Bangalore")



#For updating the subrole to Line manager
#Click on the field.
x=driver.find_element(By.XPATH,"//*[@id='mat-select-value-1']/span/span")
x.click()
#Get all the available subroles
sub_roles=driver.find_elements(By.XPATH, '//*[@id="mat-select-0-panel"]//child::span')
print(type(sub_roles))
print(len(sub_roles))
#Iterate through the list and select the "Line Manager"
for srole in sub_roles:
    if (srole.text.startswith("Line Manager")):

               srole.click()


#Click on the update button
b=driver.find_element(By.XPATH,"//*[@class='flex justify-end lg:pb-6 lg:pr-48']//child::button[@class='lg-button focus:outline-none focus:shadow-outline ng-star-inserted']")
actions = ActionChains(driver)
actions.click(b).perform()
time.sleep(2)
# panel = driver.find_element(By.XPATH, '//*[@id="mat-dialog-3"]')
# print(' Text items : ', panel.text)

#driver.switch_to.frame('cdk-overlay-pane')
#driver.switch_to.window()
#After updation Click on OK button
#ok=driver.find_element(By.XPATH,'//*[@id="mat-dialog-0"]/dialog-elements-example-dialog/div[2]/button')
ok=driver.find_element(By.XPATH,"//*[@class='flex justify-center']//child::button[@class='alrt-btn']")
ok.click()

time.sleep(5)

##############Add A new User
add=driver.find_element(By.XPATH,"/html/body/app-root/app-organization-users-list/app-navbar/mat-sidenav-container/mat-sidenav-content/div/div[1]/div[3]/a/button").click()
time.sleep(2)
print(len(driver.window_handles))
print(driver.title)
time.sleep(2)


firstname=driver.find_element(By.XPATH,"//input[starts-with(@id,'mat-input-') and @formcontrolname='firstName']")
firstname.click()
firstname.send_keys("Suma")
time.sleep(4)



lastname=driver.find_element(By.XPATH,"//input[starts-with(@id,'mat-input-') and @formcontrolname='lastName']")
lastname.click()
lastname.send_keys("S")
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/app-root/app-add-oppuser/app-navbar/mat-sidenav-container/mat-sidenav-content/div/form/div[1]/div[2]/mat-form-field[2]/div/div[1]/div/mat-select/div/div[1]').click()
# role=driver.find_elements(By.XPATH,"//*[@id='mat-select-38-panel']//child::span")
role=driver.find_elements(By.CLASS_NAME,'mat-option-text')
print(type(role))
print(len(role))
subrole='Line Manager'
for i in role:
    print(i.text)
    if(i.text == subrole):
        i.click()

time.sleep(2)

phoneno=driver.find_element(By.XPATH,'//input[starts-with(@id,"mat-input-") and @formcontrolname="phoneNumber"]')
phoneno.click()
phoneno.send_keys("9956783423")

email=driver.find_element(By.XPATH,'//input[starts-with(@id,"mat-input-") and @formcontrolname="email"]')
email.click()
email.send_keys("suma@aroha.co.in")
time.sleep(4)

#calendar=driver.find_element(By.XPATH,"/html/body/app-root/app-add-oppuser/app-navbar/mat-sidenav-container/mat-sidenav-content/div/form/div[1]/div[1]/mat-form-field[4]/div/div[1]/div[2]/mat-datepicker-toggle/button")
#calendar.click()
#time.sleep(2)
#dates=driver.find_elements(By.XPATH,"//*[@id='mat-datepicker-10']//child::div[@class='mat-calendar-body-cell-content mat-focus-indicator']")
#print(len(dates))
#time.sleep(2)

worklocation1 = driver.find_element(By.XPATH,'//input[starts-with(@id,"mat-input-") and @formcontrolname="workstation"]')
worklocation1.click()
worklocation1.send_keys("Bangalore")
button=driver.find_element(By.XPATH,"/html/body/app-root/app-add-oppuser/app-navbar/mat-sidenav-container/mat-sidenav-content/div/form/div[2]/button")
button.click()
time.sleep(2)

