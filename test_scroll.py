import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://pixabay.com/es/")
driver.maximize_window()
driver.implicitly_wait(10)
t=2
try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")))
    Buscar = driver.find_element(By.XPATH,"//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    time.sleep(t)

except TimeoutException as ex:
      print(ex.msg)
      print("El elemento no esta disponible")


driver.close()