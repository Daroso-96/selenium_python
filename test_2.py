import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Lo agrege por que antes no me servia el find_element_path

ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://demoqa.com/text-box")
time.sleep(2)
nombre = driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("Sasha")
time.sleep(2)
email = driver.find_element(By.ID,"userEmail").send_keys("sashita@dog.co")
texto1 = driver.find_element(By.ID,"currentAddress").send_keys("Probando por primera vez con selenium y python")
time.sleep(2)
texto2 = driver.find_element(By.ID,"permanentAddress").send_keys("Yuah")
time.sleep(2)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
boton = driver.find_element(By.ID,"submit").click()
time.sleep(2)
driver.close()
