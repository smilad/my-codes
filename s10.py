# def my_function(a):
#     pass

# # what is problems

# my_function(10)
# my_function("reza")
# my_function({"name": "ali","age":44})


# define by arg type

# public myString(a []int,b[]string)

from ast import Try
import re


def add(num1: int,num2: int):
    """  this  code accept two number and return summation of them

        a and b must be integer
        
        add(1,2) -> 3
     """
    return num1 + num2


# print(add("milad","ali"))



user = {"name": "ali"}

name = "milad soleymani"


help(add)

#hello milad


# help(user)




# f_list = [
#     {"name" : "milad", "age":23},
#     {"name" : " ali","age":10},
#     {"name" : "reza","age":12}
#     ]

# print(f_list)

# def update_user(name : str,**kwargs):
#     '''  update user info by name '''
#     for u in f_list:
#         if u["name"] == name:
#             u.update( )

#     return
# print(f_list)

# update_user("milad",age=333)

# print(f_list)


# def power(a,n):
#     if n == 0 :
#         return 1
    
#     return a * power(a,n-1)


# def power2(a):    
#     return a 


# print(power(2,3)) # 2 * 2 * 2

# # 2 * (2 * (2 *(1)))

# print(power2(2) * power2(2) * power2(2) *1)


# def factorial(number: int):
#     if number == 0:
#         return 1
#     return number * factorial(number - 1)


# 3

# 3 * (2 * 1 * 1)


#decorator Pattern in functions

# def my_docorator(f):
#     def wrapper():
#         print("before Start")
#         f()
#         print('after')
#     return wrapper()


# def hello():
#     print("hello")


# hello()

# my_docorator(hello)


# @my_docorator
# def printmyname():
#     print("milad")





def palindrom(inp: str):
    if len(inp) <= 1:
        return True
    a = inp[0]
    b = inp[-1]
    if a != b :
        return False
    return palindrom(inp[1:-1])


def p2(inp):
    return inp == inp[::-1]



print(palindrom("12021"))



# o(2^n)
def fibo(number):
    if number==0 :
        return 0
    if number == 1:
        return 1
    return fibo(number - 1) + fibo(number -2)


# better way

def fibo2(n):
    if n==0 :
        return 0

    a= 0
    b = 1
    for _ in range(2,n+1):
        a,b = b, a+b

    return b


def divide(a,b):
    if b == 0 :
        raise TypeError("you can not divide by zero")
    return a/b


# print(divide(4,0))



# divide(10,0)

# print(divide(10,2))


# try -> catch


# try:
#     print(divide(10,0))
# except ValueError as v:
#     print("is infinit")

# print("heloo moed")