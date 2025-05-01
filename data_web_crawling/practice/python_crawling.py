from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# 무한스크롤 함수
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

# chrome 대신 edge로 실험
driver = webdriver.Edge()
# 검색어 입력
q = input("검색어를 입력하세요 : ")
driver.get("https://www.youtube.com/results?search_query=" + q)
time.sleep(3)

elements = scroll()

title_list = []
hits_list = []

for element in elements:
    if element.get_attribute("aria-label"):
        hits_text = element.get_attribute("aria-label")
        # 조회수가 없는경우 조회수가 없음으로 표현되며, '회'라는 글자도 포함되지 않아 따로 추가함
        if (hits_text[hits_text.rfind("조회수")+4:hits_text.rfind("조회수")+6] == "없음"):
            print("조회수 없음")
        else:
            # 조회수 10000회 이상 확인
            if (int(hits_text[hits_text.rfind("조회수")+4:hits_text.rfind("회")].replace(",", "")) >= 10000):
                title_list.append(element.text)
                hits_list.append(int(hits_text[hits_text.rfind("조회수")+4:hits_text.rfind("회")].replace(",", "")))    
    else:
        print("조회수 확인 불가")

crawling_result = {
    "title" : title_list,
    "hits" : hits_list
}

dataFrame = pd.DataFrame(crawling_result)
dataFrame.sort_values(by=["title"], ascending=True).to_csv("python_crawling.csv", encoding="utf-8-sig")

okt = Okt()
word_list = []
for title in title_list:
    # print("제목", title)
    for word, tag in okt.pos(title):
        # print(word, tag)
        if tag in ['Noun', 'Adjective']:
            word_list.append(word)

# 동일 단어 횟수 추출  
word_list_count = Counter(word_list)

# 워드클라우드 객체 선언 및 출력 
wc =  WordCloud(font_path = 'NanumGothic.ttf', width=400, height=400)
result = wc.generate_from_frequencies(word_list_count)
plt.axis('off')
plt.imshow(result)
plt.show()
wc.to_file('python_cloud.png')