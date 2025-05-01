from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 브라우저 실행
driver = webdriver.Edge()
driver.get("https://www.youtube.com/feed/trending")
time.sleep(5)

titles = driver.find_elements(By.ID, "video-title")
# titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

print(titles)
for title in titles:
    # 태그 이름 가져오기
    print("태그이름 :", title.tag_name)
    # class 값 가져오기
    print("class 값 :", title.get_attribute("class"))
    # inner HTML 값 가져오기
    print("inner html 값 :", title.text)
    # 속성값 가져오기
    print("속성값 :", title.get_attribute("aria-label"))