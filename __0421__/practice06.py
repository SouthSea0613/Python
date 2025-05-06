a = []
b = [4, 5, 6]

a.append(1)
a.append(3)
a.append(2)

print(a)
print(b)

a.sort()
print(a)
print(a[1])
print(a[-2])

a[0], a[1] = a[1], a[0]
print(a)
print(len(a))
print(a.__len__())
print(a + b)