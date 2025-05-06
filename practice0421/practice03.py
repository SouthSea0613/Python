def print_hello():
    print('hello')

def return_hello():
    return 'hello'

def receive_hello(string):
    print(string)

def return_receive(string):
    return string

print_hello()
print(return_hello())
receive_hello(input("입력 : "))
print(return_receive(input("입력 : ")))