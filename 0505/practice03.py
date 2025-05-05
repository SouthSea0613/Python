import random as r

def random_num(num):
    array=[]
    for i in range(num):
        while True:
            random_sum = r.randint(1, num)
            if random_sum not in array:
                array.append(random_sum)
                break
    return array

print(random_num(10))