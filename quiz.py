# -----------------------------
# Quiz Python
# از حلقه‌ها تا Function ها
# -----------------------------


# سوال 1
# تابعی بنویس که فقط مجموع اعداد زوج را برگرداند
#
# مثال:
# sum_even([1,2,3,4,6]) -> 12

def sum_even(nums):
    pass


# سوال 2
# بدون استفاده از map پایتون
# یک map دستی بساز
#
# مثال:
# my_map([1,2,3], lambda x: x*2)
# -> [2,4,6]

def my_map(items, fn):
    pass


# سوال 3
# فیلتر با شرط
# فقط عناصری که شرط True است را برگرداند
#
# مثال:
# filter_custom([1,2,3,4,5], lambda x: x > 3)
# -> [4,5]

def filter_custom(items, condition):
    pass


# سوال 4
# pipeline ساده
# یک مقدار + لیستی از function ها بگیرد
# و همه را به ترتیب اجرا کند
#
# مثال:
#
# run(5, [
#     lambda x: x + 2,
#     lambda x: x * 3,
#     lambda x: x - 1
# ])
#
# خروجی:
# 20

def run(value, functions):
    pass


# سوال 5
# تمرین ترکیبی
#
# مراحل:
# 1. فقط اعداد فرد
# 2. توان 2
# 3. جمع نهایی
#
# مثال:
#
# process([1,2,3,4])
#
# فردها:
# [1,3]
#
# توان 2:
# [1,9]
#
# خروجی:
# 10

def process(nums):
    pass