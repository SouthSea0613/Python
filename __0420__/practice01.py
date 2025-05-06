a = 1
b = 2
print(a, b, sep = ", ")

# tmp = a
# a = b
# b = tmp
a, b = b, a
print(a, b, sep = ", ")