from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service




ser = Service("C:\drivers\geckodriver-v0.33.0-win64/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://demoqa.com/")
print(driver.title)
driver.close()