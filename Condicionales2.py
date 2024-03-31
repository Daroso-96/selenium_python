import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait, expected_conditions

ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)
driver.get("https://demoqa.com/")
driver.maximize_window()

btn=driver.find_element(By.XPATH,"//button[contains(@id,'submit')]")
print(btn.is_enabled())

if(btn.is_enabled()==True):
    print("Puedes dar click")
else:
    print("No puedes dar click")

time.sleep(2)
driver.close()