def sum2(num):
    sum = 0
    for i in range(3, num, 3):
        sum = sum + i
    return sum

print(sum2())