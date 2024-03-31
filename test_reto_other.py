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

driver.find_element(By.XPATH,"//input[contains(@name,'first_name')]").send_keys("Juan"+ Keys.TAB + "Perez" + Keys.TAB + "juan@gmail.com")
driver.find_element(By.XPATH,"//input[contains(@name,'phone')]").send_keys("3453456754"+ Keys.TAB+"Calle 643 #23"+ Keys.TAB+"CDMX")
estado=Select(driver.find_element(By.XPATH,"//select[contains(@name,'state')]"))
estado.select_by_index(5)
driver.find_element(By.XPATH,"//input[contains(@name,'zip')]").send_keys("07867"+ Keys.TAB+"demouno.com.mx")
driver.find_element(By.XPATH,"//input[contains(@value,'yes')]").click()

driver.find_element(By.XPATH,"//textarea[contains(@class,'form-control')]").send_keys("Proyecto Reto Uno"+Keys.TAB+Keys.ENTER)

driver.close()