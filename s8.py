def adder(a,b):
    return a + b


def double_it(a):
    return a * 2

def check_even(a):
    return a % 2

# a,b,c,d,...
# -> a,b
# -> a,b,c ...

# 1,2,3,4,4,5,55,...
def adder_infinit(*numbers):
    print(numbers)


adder_infinit(1,2,3) # (1,2,3)
adder_infinit(1,2) # (1,2)


# key val infinit
def myFunc(**kvargs):
    print(kvargs)
    for k,v in kvargs.items():
        print(k,v)



myFunc(name="nima",age=23)



# default arg Values

def greeting(name,country='universe'):
    print(f'hello {name} from {country}')


greeting(country='IRAN',name='alireza')




def cal(number,opt):
    return opt(number,10)

my_list = [1,2,3,4,5,6]

def caller(my_list,opt):
    for i in my_list:
        print(opt(i))


caller(my_list=my_list,opt=double_it)



# scope 

x = "name"

def sample(x):
    x2=10
    return





# Recursion

def sample(list):
    i = 0
    return i + sample(list[i+1])



a = 0
for i in range(10):
    a = a + i



def sum(*args):
    x = 0
    for i in args:
        x = x + i
    return x

def mean(*args):
    return sum(*args) / len(args)


def findBigger(*nums):
    print(max(nums)) # min for minimum


print(mean(1,2,3))
