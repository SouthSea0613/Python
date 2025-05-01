from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 엔터키 활성화
import time

# input 활용
q = input("검색어를 입력하세요 : ")

driver = webdriver.Edge()
driver.get("https://www.youtube.com/results?search_query=" + q)

time.sleep(5)
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

print(titles)
for title in titles:
    # 태그 이름 가져오기
    print("태그이름 : ", title.tag_name)
    # inner HTML 값 가져오기
    print("inner html 값 : ", title.text)
    # 속성값 가져오기
    print("속성값 : ", title.get_attribute("aria-label"))