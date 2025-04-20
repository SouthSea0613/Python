# print("정수를 입력해주세요 : ", end = "")
# int a = input()

a = int(input("정수를 입력해주세요 : "))
b = int(input("정수를 입력해주세요 : "))
print(a + b)

a = [int(input("정수를 입력해주세요 : ")) for _ in range(2)]
sum = 0
for i in a:
    sum += i
print(sum)