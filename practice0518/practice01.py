import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from practice0505 import practice01_simplified

def sort_array(array):
    for i in range(1, len(array)):
        number = array[i]
        for j in range(0, i):
            if number < array[j]:
                array[j + 1:i + 1] = array[j:i]
                array[j] = number
                break
    return array

tmp = practice01_simplified.create_random_array_simplified(10)
print(tmp)
tmp = sort_array(tmp)
print(tmp)

print(practice01_simplified.is_sorted_simplified(tmp))