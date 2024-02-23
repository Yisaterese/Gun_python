from datetime import time


def decorate(n):
    print("*********")
    print(n())
    print("*********")

#abitrary argument decorator
def decorator(n):
    def inner(*args, **kwargs):
        print("*******************")
        print(n(*args), **kwargs)
        print("******************")

    return inner



def time_taken(func):
    def wrap(*args, kwargs):
        t1 =time()
        result = func(*args, **kwargs)
        t2  = time()
        print(f"it took {t1 - t2:.3f}ms to exchange")
        return result
    return wrap

@time_taken
def get_list(number):
    result = []
    for i in range(numbers):
        result.append(i)
    return result


get_list(10000000000000)
time_taken()


@decorate
def show_name():
    return "memoriam"



@decorator
def show_name(name):
    return name
decorator() inner()

show_name("memoriam")
