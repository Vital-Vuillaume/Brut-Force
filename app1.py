from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")

chrome_service = Service(executable_path='/usr/bin/chromedriver')

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

#Put your path
driver.get("file:///home/vital/Documents/Program/Python/Brut-Force/index.html")

wait = WebDriverWait(driver, 0)

inputPassword = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="input"]')))

start = time.time()

try:
    with open('password.txt', 'r', encoding='ISO-8859-1') as file:
        for password in file:
            password = password.strip()
            
            inputPassword.send_keys(password + Keys.RETURN)
            inputPassword.clear()
                
finally:
    end = time.time()
    timePassword = end - start
    print(f"The right password: {password}")
    print(f"The time: {timePassword}")

"""
btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn"]')))
btn.click()
"""

input()