from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

driver = webdriver.Edge()
# 유튜브 정책 변경으로 인해 trending에서 실행
driver.get("https://www.youtube.com/feed/trending")

# 처음상태에서 스크롤 높이 가져오기
# selenium으로 html 콘솔 스크립트 입력하기
print(driver.execute_script("return document.documentElement.scrollHeight"))