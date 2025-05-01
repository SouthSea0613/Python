from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

driver = webdriver.Edge()
# 유튜브 정책 변경으로 인해 trending에서 실행
driver.get("https://www.youtube.com/feed/trending")

print(driver.execute_script("return document.documentElement.scrollHeight"))
# 현재 페이지의 스크롤 길이만큼 내림 = 끝까지 내림
driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")