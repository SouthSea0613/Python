from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.example.com")

p_element = driver.find_element(By.TAG_NAME, 'p')
time.sleep(5)

print(p_element)
print(p_element.text)