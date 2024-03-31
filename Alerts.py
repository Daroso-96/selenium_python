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

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")

driver.find_element(By.XPATH,"//a[@href='#myModal0']").click()
time.sleep(2)
try:
    Buscar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]" )))
    Buscar=driver.find_element(By.XPATH,"(//a[@href='#'][contains(.,'Save changes')])[1]").click()
    time.sleep(2)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")




time.sleep(4)
driver.close()


