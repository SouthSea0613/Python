word_dic = {
    "dog" : "강아지",
    "cat" : "고양이",
    "tiger" : "호랑이",
    "lion" : "사자"
}

print(word_dic["lion"]) # 키값 출력
word_dic["tiger"] = "호랭이"    # 키값 수정
print(word_dic["tiger"])    # 키값 출력
print(word_dic) # 전체 출력
word_dic["bear"] = "곰" # 키값 추가
print(word_dic) # 전체 출력