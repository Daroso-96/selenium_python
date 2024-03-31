import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)
t=2
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
driver.maximize_window()
time.sleep(2)

select1=driver.find_element(By.ID, "//select[contains(@id,'select-demo')]")
dias=Select(select1)

dias.select_by_visible_text("Sunday")
time.sleep(t)

dias.select_by_index(2)
time.sleep(t)

dias.select_by_value("Thursday")
time.sleep(t)

#segundo bloque
"""
ciudad=Select(driver.find_element_by_id("multi-select"))

ciudad.select_by_value("California")
time.sleep(t)
ciudad.select_by_value("New York")
time.sleep(t)
ciudad.select_by_index(2)
time.sleep(t)
"""

driver.close()