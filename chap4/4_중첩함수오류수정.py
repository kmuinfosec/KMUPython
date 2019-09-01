# Define Nested function
def outer_func(name):

    def inner_func():
        name = "Student" + name     # 바깥 함수의 변수 변경 시도  
        msg = "Hello, " + name
        print(msg)
    return inner_func()     # 안쪽 함수 호출


# Main program calls the function
my_name = input(“Enter your name: ")
outer_func(my_name)
