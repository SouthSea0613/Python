int_tuple = (1, 2, 3, 4)
str_tuple = ("hello", "world", "python")
mix_tuple = (10, 20, "hello")
tuple_in_tuple = (100, 200, ("inner", "tuple"), 12.345)

print(int_tuple[2])
int_tuple[2] = 10   # error 튜플은 요소의 값 변경 불가