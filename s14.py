# # users = ["alice","bob","charlie","david"]
# # for u in users:
# #     print(u)
# #
# # # value, index;
# # for i,u in enumerate(users):
# #     print(i+1,u)
# #
# #
# # # 0 -> 9
# # print(list(range(10))) #
# #
# # # start , stop - 1 , step
# # print(list(range(0,11,2)))
# #
# #
# #
# # for i in range(5):
# #     print(i)
# #
# #
# # # another alternative
# # for i  in [0,1,2,3,4,]:
# #     print(i)
# #
# #
# # ages = [23,50,33,14]
# # #zip , enumerate,
# #
# # for age,user in zip(ages,users):
# #     print(f'{user} is {age} years old')
# from unittest import case
#
# # break
# #
# # for i in range(1,5):
# #     if i % 2 == 0:
# #         print(i)
# #         break
# #
# #
# # for i in range(3):
# #     print(f'######{i}')
# #     if i % 2 == 0  :
# #         continue
# #     print(f'**{i}**')
# #     print(f'######{i}')
#
#
#
# #while (condition
#
#
#
#
#
# # sum = 0
# #
# # def calc(number, o, sumation):
# #     match o:
# #         case "+":
# #             return sumation + number
# #         case "-":
# #             return sumation - number
# #
# #
# #
# #
# # while True:
# #     a = int(input("give me a number: "))
# #     opt = input("give me an operator: ")
# #     if opt == "exit":
# #         print("bye")
# #         print("last number skipped")
# #         print(sum)
# #         break
# #     else:
# #         print(calc(a,opt,sum))
# #         sum += calc(a,opt,sum)
# #
# # print(sum)
#
#
#
# # cities = ['a','b','c'] # 3 * 3
# # matrix = []
# # for i,c1 in enumerate(cities):
# #     row = []
# #     for j,c2 in enumerate(cities):
# #         if i == j :
# #             row.append('0')
# #         else:
# #             x = input(f"what is distance between {cities[i]} and {cities[j]}?")
# #             row.append(x)
# #     matrix.append(row)
#
#
#
# cities = ['a','b'] # 3 * 3
# matrix = [['',''],['','']]
# for i,c1 in enumerate(cities):
#     for j,c2 in enumerate(cities):
#         if i == j :
#             matrix[i][j] = '0'
#         else:
#             x = input(f"what is distance between {cities[i]} and {cities[j]}?")
#             matrix[i][j] = x
#             matrix[j][i] = x
#
#
#
#
#












# list and slicing

"""

iterable type

list,string,tuple,dictionary,set

"""

xs = [10,20,30,40,50]

print(xs[0],xs[-1])

print(len(xs))
# 0 -> 4 len - 1

# can be changed

xs.append(70)
print(xs)
xs.insert(   5,60)
print(xs)

xs.remove(60)
print(xs)

xs.pop()
print(xs)

# slicing :

print(xs[1:4])
print(xs[:4])
print(xs[1::2])

print("------")
xs2 = xs[1::2]
print(xs2)
print(xs)

xs2[0] = 10000
print(xs)
print(xs2)


# tricks


ev = list(range(0,11,2))
print(ev)


print("------")

sq = [n ** 2 for n in range(1,11)]
print(sq)
print("------")

evens = [n for n in range(10) if n % 2 == 0]
print(evens)


nested_list = [[1,2,3],
               [4,5,6],
               [7,8,9]]
print(nested_list)
print(nested_list[2][1])
print(nested_list[1][2])
print(nested_list[1])


print("--- STRINGS ---")

# string
# [start:end:step]
name = "John Doe"
print(name[0])
print(name[:5])

text = '    moeid is a ai developer   '
print(text.rstrip())
print(text.lstrip())
print(text.strip())


print("moid" in text)

print(text.count("e"))

print(text.find("moeid"))


print(text.replace("moeid","radvin").strip())


strList = '1-2-3-4'

l1 = strList.split('-')
print(l1)
print(strList.split('-'))

print("+".join(l1))



# tuple ()

a = ("milad",244,False)
print(a)

name,age,isMale = a

print(name)
print(age)
print(isMale)



def x(n1,n2):
    return n1+n2,n1//n2,n1%n2

print(x(100,56))


number1 = 100
number2 = 56

# print(number1,number2)
# number1,number2 = number2,number1


# dictionary
# hash - map

user = {
    "name": "john",
    "age": 24,
}

print(user["name"])
print(user["age"])


print(user.get("x"))

# print(user['x'])

print(user.keys())
print(user.values())
print(user.items())


for i in user.items():
    print(i)


md = {n: n for n in range(10)}

matrix = {
    "ab": 100,
    "cd": 200,
}



print(md)

# set

myset = {1, 2,2,1,1,2,3, 3}
mylist2 = [1, 2,2,1,1,2,3, 3]

print(myset,mylist2)

myset.add(4)
print(myset)

myset.discard(3)
print(myset)


a = {1,2,3}
b = {2,3,4}
print("++++++")
print(a | b) #union
print('--------------')
print(a & b) # both
print('--------------')
print(a - b)
print(b - a)

print('--------------')
print(a ^ b) # excavate one


mon = {"ali", "sara" , "reza"}
tue = {"sara", "reza","mina"}

print(mon&tue)
print(mon|tue)
print(mon^mi)