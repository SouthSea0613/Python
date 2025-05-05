import random

def create_random_list(n):
    int_list = []
    for _ in range(n):
        while True:
            tmp = random.randint(0, 9)
            if tmp not in int_list:
                int_list.append(tmp)
                break
    return int_list

def is_sorted(int_list):
    for i in range(len(int_list) - 1):
        if int_list[i] > int_list[i + 1]:
            return False
    return True

a = create_random_list(2)
print(a)
print(is_sorted(a))