import practice01_simplified

def sort_array(array):
    for i in range(len(array) - 1):
        tmp_index = i
        for j in range(i + 1, len(array)):
            if array[tmp_index] > array[j]:
                tmp_index = j
        array[i], array[tmp_index] = array[tmp_index], array[i]
    return array

tmp = practice01_simplified.create_random_array_simplified(10)
print(tmp)
tmp = sort_array(tmp)
print(tmp)

print(practice01_simplified.is_sorted_simplified(tmp))