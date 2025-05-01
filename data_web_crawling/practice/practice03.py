from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# edge로도 아직까지 오류가 발생하지 않아 계속 테스트겸 사용해보는 중 입니다.
driver = webdriver.Edge()
driver.get("https://www.daum.net/")

# 검색창에 파이썬이라고 입력하고 검색버튼 클릭해보기 
search = driver.find_element(By.XPATH, '//*[@id="q"]')
search.send_keys("파이썬")
# 입력하는 것 까지 확인하고 검색 버튼 클릭
search_button = driver.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
search_button.click()
time.sleep(5)