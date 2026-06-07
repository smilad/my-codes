my_list = [1,2,3,4,5,6,7,8,9,10]
users = ['ali','reza']

# s2 = list(range(1,11,1)) == my_list
# print(s2)
# print(list(s2))

for el in my_list:
    print(el)

# i = 1,2,3,4,5,6,7.... => range()

# for i in range(len(my_list)):
#     print(my_list[i])




# user input must transform to list [1,2,3,4,5,6,7,8,9,10]
# list_user = []
# i=0
# while i <5:
#     num = int(input("give me a number: "))
#     list_user.append(num)
#     i += 1

# print(f'list of user is {list_user}')


# u = input("give me list of numbers comma separated (1,2,...): ")

# list_user = u.split(',')
# print(list_user)

# for el in list_user:
#     if not el.isdigit():
#         print(f'{el} is not a number')
#         continue
#     if int(el) % 2 == 0:
#         print(f'{el} is even')
#     else:
#         print(f'{el} is odd')




# f_list = []
# age_list = []

# while True:
#     name = input("give me a name (for stop type stop): ")
#     age = input("give me a age of that name: ")
#     if name == 'stop':
#         break
#     f_list.append(name)
#     age_list.append(age)

# print(f'list of names is {f_list}')


# for inx,name in enumerate(f_list):
#     print(f'{name} is in index {inx + 1}')


# for name,age in zip(f_list,age_list):
#     print(f'{name} is {age} years old')


# a = [1,2,3,4]
# b = ['a','b','c','d','e']

# for a,b in zip(a,b):
#     print(f'{a} is {b}')