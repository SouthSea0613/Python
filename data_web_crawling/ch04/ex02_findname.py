names = ["김파이", "이파이", "박파이", "최파이"]
search_name = input("이름을 입력하세요 : ")
#print(search_name)

for name in names:
    if search_name == name:
        print("이름이 있습니다.")
        print(name.index(name))

if search_name in names:
    print("이름이 있습니다.")
    print(name.index(name))
else:
    print("이름이 없습니다.")