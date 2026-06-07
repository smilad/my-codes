# Function / Recursion / *args / **kwargs Exercises




# 1) شمارش تعداد حروف رشته

def count_chars(text):
    return len(text)

# مثال:
# count_chars("hello") -> 5


# 2) برعکس کردن رشته

def reverse_text(text):
    return text[::-1]

# مثال:
# reverse_text("python") -> "nohtyp"


# ---------------- RECURSION ----------------


# 6) فاکتوریل

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# مثال:
# factorial(5) -> 120


# 7) توان عدد

def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

# مثال:
# power(2, 5) -> 32


# 8) جمع اعداد 1 تا n

def sum_to_n(n):
    if n <= 1:
        return n
    return n + sum_to_n(n - 1)

# مثال:
# sum_to_n(5) -> 15


# 9) فیبوناچی

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# مثال:
# fib(6) -> 8


# 10) جمع عناصر لیست با recursion

def recursive_sum(nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(nums[1:])

# مثال:
# recursive_sum([1,2,3,4]) -> 10


# 11) palindrome با recursion

def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

# مثال:
# is_palindrome("level") -> True


# 12) countdown recursive

def countdown(n):
    if n <= 0:
        print("Done")
        return
    print(n)
    countdown(n - 1)

# مثال:
# countdown(5)
#
# 5
# 4
# 3
# 2
# 1
# Done


# ---------------- *args ----------------


# 13) جمع همه ورودی‌ها

def total(*args):
    return sum(args)

# مثال:
# total(1,2,3,4) -> 10


# 14) پیدا کردن بزرگ‌ترین مقدار

def find_max(*args):
    return max(args)

# مثال:
# find_max(4,7,2) -> 7


# 15) میانگین اعداد

def average(*args):
    return sum(args) / len(args)

# مثال:
# average(2,4,6) -> 4


# 16) چاپ همه آرگومان‌ها

def print_all(*args):
    for arg in args:
        print(arg)

# مثال:
# print_all(1, "hello", True)


# ---------------- **kwargs ----------------


# 17) چاپ key و value

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# مثال:
# show_info(name="Ali", age=20)


# 18) شمارش تعداد keyها

def count_keys(**kwargs):
    return len(kwargs)

# مثال:
# count_keys(a=1, b=2, c=3) -> 3


# 19) ساخت پروفایل کاربر

def create_user(**kwargs):
    return kwargs

# مثال:
# create_user(name="Sara", city="Tehran")


# ---------------- ترکیبی ----------------


# 20) استفاده همزمان از args و kwargs

def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

# مثال:
# demo(1,2,3,name="Ali", age=25)


# 21) mini print function

def my_print(*args, sep="-"):
    print(sep.join(str(a) for a in args))

# مثال:
# my_print(1,2,3)
#
# خروجی:
# 1-2-3


# 22) ماشین حساب

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# 23) Recursive minimum

def recursive_min(nums):
    if len(nums) == 1:
        return nums[0]
    rest_min = recursive_min(nums[1:])
    return nums[0] if nums[0] < rest_min else rest_min

# مثال:
# recursive_min([4,1,8,2]) -> 1


# 24) logger function

def log(**kwargs):
    parts = [f"{k}={v}" for k, v in kwargs.items()]
    print("[" + ", ".join(parts) + "]")

# مثال:
# log(level="INFO", message="server started")


# 25) recursive power بدون استفاده از **

def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

# مثال:
# power(2,10) -> 1024