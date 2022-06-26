from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


service = Service('chromedriverPath')
driver = webdriver.Chrome(service=service)

driver.get('http://orteil.dashnet.org/experiments/cookie/')
x = True
cookie = driver.find_element(By.ID, 'cookie')

time_to_check = time.time() + 15



while x:
    cookie.click()
    if time.time() > time_to_check:
        money = driver.find_element(By.CSS_SELECTOR, '#money')
        print(money.text)
        cost = driver.find_elements(By.CSS_SELECTOR, "#store > div")
        for item in cost[::-1]:
            color = item.get_attribute("class")
            if color != "grayed":
                item.click()
                break
        time_to_check = time.time() + 15

driver.quit()
