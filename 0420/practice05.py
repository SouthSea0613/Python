# print("정수를 입력해주세요 : ", end = "")
# int a = input()

a = int(input("정수를 입력해주세요 : "))
b = int(input("정수를 입력해주세요 : "))
print(a + b)

print(sum([int(input("정수를 입력해주세요 : ")) for _ in range(int(input("몇개를 입력받을지 입력해주세요 : ")))]))