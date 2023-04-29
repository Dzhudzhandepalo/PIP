import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
time.sleep(5) 
driver.get("https://rozetka.com.ua/ua/")
time.sleep(5)

dom_input = driver.find_element(by=By.NAME, value='search')
time.sleep(5)
# Mobile phone Samsung search
dom_input.send_keys("Мобільний телефон Samsung")
dom_input.send_keys(Keys.ENTER)
time.sleep(5)