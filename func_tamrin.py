# 1) جمع اعداد لیست
# تابعی بنویس که مجموع یک لیست عدد را با for حساب کند

def sum_list(nums):
    total = 0

    for num in nums:
        total += num

    return total


# 2) فیلتر اعداد زوج
# فقط اعداد زوج را چاپ یا برگرداند

def filter_even(nums):
    result = []

    for num in nums:
        if num % 2 == 0:
            result.append(num)

    return result


# 3) توان 2 روی لیست
# هر عدد را به توان 2 برسان

def square_list(nums):
    result = []

    for num in nums:
        result.append(num ** 2)

    return result


# 4) apply function
# یک لیست و یک تابع بگیرد و روی همه اعمال کند

def apply(items, fn):
    result = []

    for item in items:
        result.append(fn(item))

    return result


# 5) فیلتر با شرط دلخواه (lambda)
# فقط عناصری که شرط true است را برگرداند

def filter_custom(items, condition):
    result = []

    for item in items:
        if condition(item):
            result.append(item)

    return result


# 6) شمارش با شرط
# تعداد عناصر مطابق شرط را برگرداند

def count_if(items, condition):
    count = 0

    for item in items:
        if condition(item):
            count += 1

    return count


# 7) ماشین حساب فانکشنی
# دو عدد + یک function (operation)

def calc(a, b, op):
    return op(a, b)


# 8) map دستی (بدون map پایتون)
# نسخه ساده map بساز

def my_map(items, fn):
    result = []

    for item in items:
        result.append(fn(item))

    return result


# 9) pipeline (ترکیب فانکشن‌ها)
# یک مقدار + لیستی از فانکشن‌ها

def run(value, functions):
    result = value

    for fn in functions:
        result = fn(result)

    return result


# 10) تمرین ترکیبی (mini pipeline واقعی)
# 1. زوج‌ها
# 2. ضربدر 10
# 3. جمع نهایی

def is_even(x):
    return x % 2 == 0


def multiply_by_10(x):
    return x * 10


def sum_all(nums):
    total = 0

    for num in nums:
        total += num

    return total


def process(nums):
    # مرحله 1: فقط زوج‌ها
    evens = filter_custom(nums, is_even)

    # مرحله 2: ضربدر 10
    multiplied = my_map(evens, multiply_by_10)

    # مرحله 3: جمع نهایی
    return sum_all(multiplied)


# تست
print(sum_list([1, 2, 3, 4]))          # 10
print(filter_even([1, 2, 3, 4, 6]))   # [2, 4, 6]
print(square_list([1, 2, 3]))         # [1, 4, 9]

print(calc(10, 5, lambda a, b: a+b))  # 15
print(calc(10, 5, lambda a, b: a*b))  # 50

print(process([1, 2, 3, 4]))
