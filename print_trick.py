# تریک‌های مختلف formatting در print و f-string

name = "Alice"
age = 27
score = 91.756
number = 42

print("=== Basic Formatting ===")

# راست‌چین
print(f"|{number:10}|")

# چپ‌چین
print(f"|{number:<10}|")

# وسط‌چین
print(f"|{number:^10}|")

# پر کردن با صفر
print(f"|{number:010}|")

# تعداد رقم اعشار
print(f"|{score:.2f}|")

# درصد
ratio = 0.8732
print(f"|{ratio:.1%}|")

# جداکننده هزارگان
big = 1234567890
print(f"|{big:,}|")

# نمایش هگز
print(f"|{number:x}|")

# نمایش باینری
print(f"|{number:b}|")

# نمایش علمی
print(f"|{score:e}|")

print("\n=== Table Example ===")

# جدول خوش‌فرمت
users = [
    ("Alice", 27, 91.7),
    ("Bob", 31, 88.2),
    ("Charlie", 22, 95.9),
]

# header
print(f"{'Name':<12}{'Age':<8}{'Score':<10}")
print("-" * 30)

# rows
for name, age, score in users:
    print(f"{name:<12}{age:<8}{score:<10.2f}")