# 1) Install venv 
# 2) Install selenium
# 3) Open http://www.rozetka.ua in Mozila Firefox 
# 4) Find input (searcher) from rozetka
# 5) Write there : “Samsung” / or other mark that you want 
# 6) Press Enter via Selenium WebDriver
# 7) Send me gitHub link on your homework

# * 
# On the GitHub you should have next branches :
# - Developer
# - Main 
# - Hotfix
# - QA -> your homework
# - Feature 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
# browser Firefox
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

# browser Chrome
driver = webdriver.Chrome()
time.sleep(5) 
driver.get("https://rozetka.com.ua/ua/")
time.sleep(5)

dom_input = driver.find_element(by=By.NAME, value='search')
time.sleep(5)
# Mobile phone Apple search
dom_input.send_keys("Мобільні телефони Apple")
dom_input.send_keys(Keys.ENTER)
time.sleep(15)