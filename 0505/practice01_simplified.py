import random

def create_random_array_simplified(number):
    return random.sample(range(number), number)

def is_sorted_simplified(array):
    return array == sorted(array)