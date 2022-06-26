from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service('/Users/ryanford/Desktop/Development/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Ryan")
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys("Ford")
email = driver.find_element(By.NAME, "email")
email.send_keys("Ryanford96@yahoo.com")

send = driver.find_element(By.CSS_SELECTOR, 'form button')
send.click()