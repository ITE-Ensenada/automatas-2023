from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.google.com")
##assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("ensenada")
elem.send_keys(Keys.RETURN)
time.sleep(15)
elem = driver.find_element(By.NAME, "q")
elem.send_keys(Keys.PAGE_DOWN)
elem.send_keys(Keys.PAGE_DOWN)
assert "No results found." not in driver.page_source
#driver.close()