import random

def create_random_array(number):
    array = []
    for _ in range(number):
        while True:
            tmp = random.randint(0, 99)
            if tmp not in array:
                array.append(tmp)
                break
    return array

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True