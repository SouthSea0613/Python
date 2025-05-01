from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ex01_scroll.py 함수화
def scroll():
    while True:
        before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(1)
        after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        if before_scroll_height == after_scroll_height:
            break

    time.sleep(3)

driver = webdriver.Edge()
# 유튜브 정책 변경으로 인해 특정 검색에서 실행
driver.get("https://www.youtube.com/results?search_query=lck")

# 함수실행
scroll()

# XPATH로 제목 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

print("영상 갯수 :", len(titles))
for title in titles:
    print(title.text)