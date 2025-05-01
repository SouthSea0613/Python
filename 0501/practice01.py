import math

while True:
    number = int(input())
    if number == -1:
        break
    else:
        numbers = [1]
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                numbers.append(i)
                if i != number // i:
                    numbers.append(number // i)

        print(sum(numbers))
        print(numbers)