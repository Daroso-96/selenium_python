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

name = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Sasha")
Lastname = driver.find_element(By.XPATH, "//input[contains(@name,'last_name')]").send_keys("Dog")
email = driver.find_element(By.XPATH, "//input[contains(@name,'email')]").send_keys("sasha@dog.com")
phone = driver.find_element(By.XPATH, "//input[contains(@name,'phone')]").send_keys("555875235")
address = driver.find_element(By.XPATH, "//input[contains(@name,'address')]").send_keys("st.19a#23")
city = driver.find_element(By.XPATH, "//input[contains(@name,'city')]").send_keys("Miami")
state = Select(driver.find_element(By.XPATH,"//select[contains(@name,'state')]"))
state.select_by_index(10)
zipcode = driver.find_element(By.XPATH, "//input[contains(@name,'zip')]").send_keys("07867")
website = driver.find_element(By.XPATH, "//input[contains(@name,'website')]").send_keys("sashitadog.com")
btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'yes')]")))
btn1.click()
project_description = driver.find_element(By.XPATH, "//textarea[contains(@class,'form-control')]").send_keys("No sé un proyecto random")
boton = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]").click()



time.sleep(t)




driver.close()