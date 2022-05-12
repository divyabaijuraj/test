import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()

frame_ele = driver.find_element(By.XPATH, '//*[@id="content"]/iframe')

driver.switch_to.frame(frame_ele)

drag_ele = driver.find_element(By.ID, "draggable")
drop_ele = driver.find_element(By.ID, "droppable")

time.sleep(2)
action_obj = webdriver.ActionChains(driver)

action_obj.drag_and_drop(drag_ele, drop_ele).perform()

time.sleep(10)
