# =========================
# 1
# =========================
# برنامه‌ای بنویسید که یک عدد بگیرد و مشخص کند مثبت است، منفی است یا صفر.

num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# =========================
# 2
# =========================
# برنامه‌ای بنویسید که دو عدد بگیرد و بزرگ‌ترین را چاپ کند.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a)
else:
    print(b)


# =========================
# 3
# =========================
# برنامه‌ای بنویسید که اعداد 1 تا n را چاپ کند.

n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i)
    i += 1


# =========================
# 4
# =========================
# برنامه‌ای بنویسید که مجموع اعداد 1 تا n را محاسبه کند.

n = int(input("Enter n: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)


# =========================
# 5
# =========================
# برنامه‌ای بنویسید که بزرگ‌ترین رقم یک عدد را پیدا کند.

num = int(input("Enter number: "))

max_digit = 0

while num > 0:

    digit = num % 10

    if digit > max_digit:
        max_digit = digit

    num = num // 10

print("Largest digit =", max_digit)


# =========================
# 6
# =========================
# برنامه‌ای بنویسید که بررسی کند یک عدد پالیندروم (قرینه) است یا نه.

num = int(input("Enter number: "))

original = num
reverse = 0

while num > 0:

    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not palindrome")


# =========================
# 7
# =========================
# برنامه حدس عدد بنویسید.

secret = 7

while True:

    guess = int(input("Guess number: "))

    if guess == secret:
        print("Correct!")
        break

    if guess < secret:
        print("Bigger")
    else:
        print("Smaller")


# =========================
# 8
# =========================
# برنامه‌ای بنویسید که از کاربر عدد بگیرد تا زمانی که صفر وارد شود، سپس مجموع را چاپ کند.

total = 0

while True:

    num = int(input("Enter number: "))

    if num == 0:
        break

    total += num

print("Sum =", total)


# =========================
# 9
# =========================
# برنامه‌ای بنویسید که اگر عدد 999 وارد شد، برنامه متوقف شود.

while True:

    num = int(input("Enter number: "))

    if num == 999:
        break

    print(num)

print("Program stopped")


# =========================
# 10
# =========================
# برنامه‌ای بنویسید که اعداد 1 تا 20 را چاپ کند به جز مضرب‌های 3.

i = 0

while i < 20:

    i += 1

    if i % 3 == 0:
        continue

    print(i)


# =========================
# 11
# =========================
# برنامه‌ای بنویسید که جدول ضرب یک عدد n را چاپ کند.

n = int(input("Enter number: "))

i = 1

while i <= 10:
    print(n, "*", i, "=", n * i)
    i += 1


# =========================
# 12
# =========================
# برنامه‌ای بنویسید که بررسی کند یک عدد اول است یا نه.

num = int(input("Enter number: "))

i = 2
is_prime = True

if num <= 1:
    is_prime = False

while i < num:

    if num % i == 0:
        is_prime = False
        break

    i += 1

if is_prime:
    print("Prime")
else:
    print("Not prime")


# =========================
# 13
# =========================
# برنامه‌ای بنویسید که الگوی زیر را چاپ کند:
# *
# **
# ***
# ****

i = 1

while i <= 4:
    print("*" * i)
    i += 1


# =========================
# 14
# =========================
# برنامه‌ای بنویسید که الگوی زیر را چاپ کند:
# ****
# ***
# **
# *

i = 4

while i >= 1:
    print("*" * i)
    i -= 1