from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('/Users/ryanford/Desktop/Development/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
# driver.get("https://www.amazon.com/SimpliSafe-Camera-1080p-Compatible-Security/dp/B089PYDDVY/ref=sr_1_13?crid=1UG0CKVPGGJEA&keywords=simplisafe&qid=1640261859&sprefix=simplisafe%2Caps%2C83&sr=8-13")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.get_attribute("innerHTML"))
event_dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')


events = {}

for n in range(len(event_dates)):
    events[n] = {
        "time": event_dates[n].text,
        "name": event_names[n].text,
    }

print(events)

# print(d)
driver.quit()