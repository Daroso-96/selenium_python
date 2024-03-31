import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Lo agrege por que antes no me servia el find_element_path
#El implicit wait es esperar si encuentra un objeto
ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)
driver.get("https://coink.com/")
driver.maximize_window()
driver.implicitly_wait(10)
t= 3
driver.find_element(By.ID,"//div[@id='sg-popup-content-wrapper-8095']").click()


time.sleep(t)
driver.close()