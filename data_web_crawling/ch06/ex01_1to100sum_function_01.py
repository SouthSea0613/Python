def sum1():
    sum = 0
    for i in range(3, 101, 3):
        sum = sum + i
    return sum

print(sum1())