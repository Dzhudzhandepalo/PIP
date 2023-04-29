import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# service = FirefoxService(executable_path=GeckoDriverManager().install()) # Тут ми кожен раз качаємо драйвер, тому не потрібно його качати.

# rozetka = "https://rozetka.com.ua/ua/"

driver = webdriver.Firefox()
time.sleep(5)
driver.get("https://rozetka.com.ua/ua/")
time.sleep(5)

search_but = driver.find_element(by=By.NAME, value="search")
# submit_button = driver.find_elements(by=By.CSS_SELECTOR, value="Знайти")
time.sleep(5)

search_but.send_keys("samsung")
search_but.send_keys(Keys.ENTER)

# message = driver.find_elements(by=By.ID, value="samsung")
# value = message.text
# assert value == "Received!"



time.sleep(5) # Let the user actually see something!

# driver.quit()