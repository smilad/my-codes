



# age = int(input("give me your age : "))
# name = input("what is your name: ")

# # shorter if or ternary operetor
# elig =  True if age > 18 else False


#  # normal if
# # elig =False
# # if age > 18 :
# #     elig = True


# strr = 'hello ' + name + 'your eligiblity is' + str(elig)

# print(strr)
# print(f'hello {name} : you are eligiblity is : {elig}')


# match age:
#     case "+":
#         print('10')
#     case "-":
#         print('20')
    









# num_1 = int(input("give me first num :"))
# num_2 = int(input("give me seconf num :"))
# opt = input("give me your operator: ( + | - | * | /)")



# match opt:
#     case "+":
#         print(num_1 + num_2)
#     case "-":
#         pass
#     case "/":
#         pass
#     case "*":
#         pass
#     case _ :
#         print("there is err")




x = int(input("give me x axis: "))
y = int(input("give me y axis: "))

print(f"area is {x * y} and env is {(x + y)*2}")




num1 = int(input("give me first num :"))
num2 = int(input("give me sec num :"))
num3 = int(input("give me third num :"))

if num1 > num2 and num1 > num3 :
    pass
elif num2 > num1 and num2 > num3:
    pass
else:
    pass

max = max(num1,num2,num3)
print(max)



name = input("input your name *:") #
lname = input("input your last name*:") #
age = input("input age") #
number = input("input number*")
email = input("input your mail")
gender= input ("input your gender( male | female)")


# error = True if len (name) == 0 or len(lname) == 0 or len(number) == 0 else Fa


if len (name) == 0 or len(lname) == 0 or len(number) == 0:
    print("error in data")
else:
    # if gender == 'male':
    #     print (f'wellcome mr {name}')
    # else:
    #     print(f'wellcome mss {name}')
    match gender:
        case "male":
            pass
        case "female":
            pass
        case _ :
            print("are you human at all ??")

