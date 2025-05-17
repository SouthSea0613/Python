import random as r

def random_num(num):
    array=[]
    for i in range(num):
        while True:
            random_sum = r.randint(1,num)
            if random_sum not in array:
                array.append(random_sum)
                break
    return array

def array_sort(array):
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            return False
    return True

print(array_sort(random_num(10)))