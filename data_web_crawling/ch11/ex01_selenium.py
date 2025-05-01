# selenium 모듈 추가 
from selenium import webdriver
# 딜레이 추가
import time

# 브라우저(크롬) 실행
# driver = webdriver.Chrome()
# 난 edge로 해봄
driver = webdriver.Edge()
# 주소 입력(구글 홈페이지)
driver.get("https://www.google.com")
# 딜레이 추가
time.sleep(5)