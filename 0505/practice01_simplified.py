import random

def create_random_list_simplified(number):
    return random.sample(range(number), number)

def is_sorted_simplified(array):
    return array == sorted(array)