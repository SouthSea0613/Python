from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://comic.naver.com/webtoon")
time.sleep(2)
webtoon_titles = driver.find_elements(By.CLASS_NAME, 'ContentTitle__title_area--x24vt')
time.sleep(5)
for name in webtoon_titles:
    print(name.text)
print(len(webtoon_titles))