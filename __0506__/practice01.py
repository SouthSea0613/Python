import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from __0505__ import practice01_simplified

def sort_array(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

tmp = practice01_simplified.create_random_array_simplified(10)
print(tmp)
tmp = sort_array(tmp)
print(tmp)

print(practice01_simplified.is_sorted_simplified(tmp))