count = 1
bool_var = True
while bool_var:
    print("hello", count)
    if count == 10:
        bool_var = False
    count = count + 1

print(count)