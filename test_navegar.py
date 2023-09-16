import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
t=3
ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://www.selenium.dev/documentation/webdriver/elements/finders/")
time.sleep(t)

driver.get("https://inmanga.com/ver/manga/Billy-Bat/04/16095152-e142-450a-9b41-28b60f8db8ba")
time.sleep(t)

driver.get("https://artoftesting.com/press-enter-tab-space-arrow-function-keys-in-selenium-webdriver-with-java")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.close()