from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scroll():
    while True:
        before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        # 로딩시간 확보
        time.sleep(3)
        after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        if before_scroll_height == after_scroll_height:
            break

    # XPATH로 제목 가져오기            
    return driver.find_elements(By.XPATH, '//*[@id="video-title"]')

driver = webdriver.Edge()
# 유튜브 정책 변경으로 인해 trending에서 실행
driver.get("https://www.youtube.com/feed/trending/")
time.sleep(3)

elements = scroll()

hits_list = []
title_list = []

for element in elements:
    if element.get_attribute("aria-label"):
        hits_text = element.get_attribute("aria-label")
        title_list.append(element.text)
        hits_list.append(int(hits_text[hits_text.rfind("조회수")+4:hits_text.rfind("회")].replace(",", "")))
    else:
        print("조회수 데이터 없음")

for title, hits in zip(title_list, hits_list):
    print(title, ":", hits)