# def printMyName():
#     print("hello milad")


# def printMyAge():
#     print("hello i am 30")




# def my_decorator2(func):
#     def w():
#         print("start of code")
#         func()
#         print("end od code execution")

#     return w()






def my_decorator(f):
    def wrapper():
        print("start to execution")
        f()
        print('end of excution')
    return wrapper()

# @my_decorator
# def hello():
#     print("hello i am Hero")


# hello()




def decorator(f):
    def wrapper(*args,**kwargs):
        try:
            result = f(*args,**kwargs)
            return result.upper()
        except ValueError as v:
            print("ERROR: WTH is this")
    return wrapper


def decorator2(f: function):
    def wrapper(*args,**kwargs):
        print(f"Strating to run {f.__name__}")
        result = f(*args,**kwargs)
        # if result < 0:
        return "END"
    return wrapper

import time

def doing_time(f: function):
    def wrapper(*args,**kwargs):
        st = time.perf_counter()
        f()
        end = time.perf_counter()
        print(end - st)
    return wrapper


@doing_time
def say_hello():
    time.sleep(5)
    print("hello")


@decorator2
def capitalize(name="milad"):
    return name

# def wrapper(*args,**kwargs):
#         print("there is inside decorator")
#         result = capitalize(*args,**kwargs)
#         print(result.lower())
#         # if result < 0:
#         return result


print(say_hello())

