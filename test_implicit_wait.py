import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Lo agrege por que antes no me servia el find_element_path
#El implicit wait es esperar si encuentra un objeto
ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)
t= 1
driver.get("https://demoqa.com/text-box")
driver.implicitly_wait(10)
time.sleep(t)
nombre = driver.find_element(By.XPATH,"//*[@id='userName']")
nombre.send_keys("Sasha")
time.sleep(t)
email = driver.find_element(By.XPATH,"//input[@id='userEmail']")
email.send_keys("sashita@dog.co")
texto1 = driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
texto1.send_keys("Probando por primera vez con selenium y python")
time.sleep(t)
texto2 = driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys("Yuah")
time.sleep(t)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(t)
boton = driver.find_element(By.XPATH,"//button[@id='submit']").click()
time.sleep(t)
driver.close()