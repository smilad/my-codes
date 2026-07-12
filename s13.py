

# \n end default value


print("hello",'world',sep="...",end="!!! \n")

print("loading",end="\n")


# age = input("what is your age?")

# print(type(age))

# type casting

# age = int(age)
# print(type(age))


#formated string or(f-string)

name = "milad"
bookcount = 3


print(f'{name} has {bookcount * 2} books')




def prettifier(s: str) -> str:
    return '****' + s + '****'

print(f'{name} has {prettifier(str(bookcount))} books')


price = 740 #float

pi = 3.142516

print(f'price is {pi:.2f} dollars')

print(f'normal price{price} padding{price:4d}')

# print(f'{'hi':>10}')
# print(f'{'hi':^10}')
# print(f'{'hi':<10}')


print(f'{'|':<10} {'name':^10} {'|':^10} {'age':^10} {'|':>10}')
print(f'{'|':<10} {'milad':^10} {'|':^10} {'30':^10} {'|':>10}')




# type casting:

x=10
y=5.45
name = 'akbar'
isOK= True
print(type(x), type(y), type(isOK), type(name))

print(float(x))
print(int(y))
print(bool(name))
print(bool('')) #[] 0 -> truthy - falsy

print(int(isOK))
# number = 0
# if number == 0 :
#     print('number is not zero1')
#
# if not number :
#     print('number is not zero2')


# bases of number: binary - hex - deca and etc...

print(0b0100,0o17,0xff)

n= 255

print(f'{n:b},{n:o},{n:x}')



#operators

# Arithmetic operator

# + - / *
# // ** %

print(10 + 2, 10 -2, 10/2, 10//3, 10**2, 10 % 7)


# comparison operators

print (5>2,5==5, 5!= 4)
x = 7 # -> assignment operator

age = 20
member = False

print (age >= 20 and member) # or , not

# precedence

print(2 + 4 * 3)

# * / // % then + -

print((2+3)*4)

# making decision


# boolean

age = 18

if age >= 30:
    print('you are old')
elif 20 <= age < 30: # 20 ..... 30
    print('you are not old')
else:
    print('you are a child')

# one line decision making

isNewUser = False

label = "new user" if isNewUser else "old user"



match label:
    case 'new user':
        print(f'{label} ')
    case 'old user':
        print(f'{label} ')
    case _:
        print('?????')

















#






