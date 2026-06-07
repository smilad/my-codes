# # def name(arg1 , arg2 ,....) -> return args:
# #     pass



# # def add_two_num(num_1,num_2):
# #     return num_1+num_2
    


# # name = 'mohammad'
# # def printname(name):
# #     name = 'ali'
# #     # age = 23
# #     print(f"my name is {name}")
# #     return

# # # printname(name)
# # # print(age)


# # def say_hello_to_user(name='user',greeting='wellcom'):
# #     print(f'{greeting} mr. {name}')


# # say_hello_to_user()
# # say_hello_to_user("ali","Hola")
# # say_hello_to_user(greeting='hello')




# from numbers import Integral


# def find_prime(number):
#     primes = [2,3,5,7]
#     if number in primes:
#         return True
#     elif number %2 == 0 or number % 3== 0 or number % 5 == 0 or number %7 == 0 :
#         return False
#     return True


# def check_my_number_status(number):
#     status = find_prime(number)
#     if status :
#         print(f'your number is prime')
#         # return -> if you dont want to user ELSE
#     else:
#         print('your number is not prime')

# # def check_my_number_status2(number):
# #     status = find_prime(number)
# #     if status :
# #         print(f'your number is prime')
# #         return #
# #     print('your number is not prime')

# check_my_number_status(13)
# check_my_number_status(10)


# def gcd_cal(a,b):
#     while b!=0:
#         a,b = b,a%b
#     return a


# a = int(input("give me one number : "))
# b = int(input("give me one number : "))

# print(gcd_cal(a,b))





# i= 0
# while i< 5:
#     print("***")
#     i+=1
#     print(i)

# while True:

# range(start,stop,step)

# print(list(range(1,10,2)))
# print(list(range(10)))

# for i in range(5):
#     print("***")
#     print(i)
#     print('***')


# for i in [0,1,2,3,4]:

# l =["a","b","c","d"]

# # for i in l :
# #     print(i)

# for index,v in enumerate(l):
#     print(index,v)


# u = ['reza','melika','alireza']
# age = ['55','107','45']

# for u,a in zip(u,age):
#     print(f'{u} is {a} years old')



# def sample(a):
#     if a == 0:
#         return
#     print(a)
#     sample(a - 1)


# sample(10)

import re


def add(*num):
    print(num)


def square(x):
    x**2


square2 = lambda x: print(x)

# ageCheck = lambda x : x >= 20

# def ageCheck(x):
#     return x >= 20

square(4)
print(ageCheck(10))













