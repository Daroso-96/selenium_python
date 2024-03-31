import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait, expected_conditions

ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get('http://autopract.com/selenium/alert5/')

driver.find_element(By.ID, 'alert-button').click()
alert = Alert(driver)
print(alert.text)
alert.accept()
driver.find_element(By.ID,'confirm-button').click()
alert.dismiss()