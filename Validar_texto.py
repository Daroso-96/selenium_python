import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=2
btn = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]").click()
time.sleep(t)

name_val=driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")
name=name_val.text
print("El valor del error es:" +name)
if(name=="Please supply your first name"):
      #print("Falta el nombre")
      name_correct = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Sasha")
      time.sleep(2)
      print("Nombre correcto")
else:
    print("Falta el nombre")
driver.close()