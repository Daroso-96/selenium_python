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

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=2
try:
   Buscar = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'fileinput')]")))
   Buscar = driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
   Buscar.send_keys("D:\seleniunpython\imagenes\demo1.jpg")
   time.sleep(t)
   driver.find_element(By.XPATH, "//input[contains(@id,'itsanimage')]").click()
   driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()

except TimeoutException as ex:
      print(ex.msg)
      print("El elemento no esta disponible")


driver.close()