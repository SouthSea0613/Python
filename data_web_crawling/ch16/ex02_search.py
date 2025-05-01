from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
# 주소값으로 검색하는 방법
driver.get("https://www.youtube.com/results?search_query=omega+protocol")

time.sleep(5)
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

print(titles)
for title in titles:
    # 태그 이름 가져오기
    print("태그이름 :", title.__class__)
    # inner HTML 값 가져오기
    print("inner html 값 :", title.text)
    # 속성값 가져오기
    print("속성값 :", title.get_attribute("aria-label"))