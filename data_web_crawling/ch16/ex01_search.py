from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 엔터키 활성화
# import time

driver = webdriver.Edge()
driver.get("https://www.youtube.com/")

search_input = driver.find_element(By.CSS_SELECTOR, "input#search")
search_input.send_keys("omega protocol")

# 검색 버튼을 찾아서 클릭하는 코드 두줄
# search_button = driver.find_element(By.CSS_SELECTOR, "button#search-icon-legacy")
# search_button.click()

# 엔터키를 누르는 동작
search_input.send_keys(Keys.RETURN)

# time.sleep(5)
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

print(titles)
for title in titles:
    # 태그 이름 가져오기
    print("태그이름 :", title.tag_name)
    # inner HTML 값 가져오기
    print("inner html 값 :", title.text)
    # 속성값 가져오기
    print("속성값 :", title.get_attribute("aria-label"))