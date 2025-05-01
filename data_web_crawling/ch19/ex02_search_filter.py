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
driver.get("https://www.youtube.com/")
time.sleep(3)

# 검색어 입력
search_input = driver.find_element(By.CSS_SELECTOR, "input#search")
search_input.send_keys("트럼프")
time.sleep(3)

# 검색버튼 클릭
search_button = driver.find_element(By.CSS_SELECTOR, "button#search-icon-legacy")
search_button.click()
time.sleep(3)

# 필터버튼의 XPATH값
filter_button = driver.find_element(By.XPATH, '//*[@id="filter-button"]')
filter_button.click()
time.sleep(3)

# 동일한 값이 여러개 존재하여 full XPATH 값 복사
hits_button = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a')
hits_button.click()
time.sleep(3)

titles = scroll()

for title in titles:
    print(title.text)
print("영상 갯수 :", len(titles))