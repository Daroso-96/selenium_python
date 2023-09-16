import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Lo agrege por que antes no me servia el find_element_path

ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://demoqa.com/text-box")
time.sleep(2)
nombre = driver.find_element(By.XPATH, "//input[contains(@id,'userName') and @id='userName']").send_keys("Sasha")
nombre.send_keys(Keys.TAB + "sashita@dog.com" + Keys.TAB + "Direcccion uno" + Keys.TAB + "Direccion dos " + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element(By.XPATH,"(//span[contains(@class,'text')])[2]").click()
time.sleep(2)
driver.close()
