import random
import statistics

number_list = []
for _ in range(10000):
    number_list.append(random.randint(0, 1))

print(statistics.mean(number_list))