import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=2

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[4]")))
btn1.click()

btn3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[6]")))
btn3.click()

btn4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[7]")))
btn4.click()




driver.execute_script("window.scrollTo(0,300)")

time.sleep(t)
driver.close()