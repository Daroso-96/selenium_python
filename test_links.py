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
#Obteniendo todos los links de la pàgina
links=driver.find_elements(By.TAG_NAME,"a")

print("El numero de Links que hay en la pàgina es: ",len(links))

for num in links:
    print(num.text)

driver.find_element(By.LINK_TEXT,"Date pickers").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT,"JQuery Date Picker").click()
time.sleep(t)







time.sleep(t)
driver.close()