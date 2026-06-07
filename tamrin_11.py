# ------------------------------------------
# ------------------------------------------
# یک دکوراتور بنویس به اسم say_start
# که قبل از اجرای فانکشن چاپ کنه:
# "--- شروع ---"
#
# مثال خروجی:
#     --- شروع ---
#     سلام!

def say_start(func):
    def wrapper():
        pass  # کدت اینجا
    return wrapper

@say_start
def greet():
    print("سلام!")

greet()


# ------------------------------------------
# ------------------------------------------
# یک دکوراتور بنویس به اسم border
# که قبل از فانکشن چاپ کنه: "=========="
# و بعد از فانکشن هم چاپ کنه: "=========="
#
# مثال خروجی:
#     ==========
#     من یک برنامه‌نویسم!
#     ==========

def border(func):
    def wrapper():
        pass  # کدت اینجا
    return wrapper

@border
def introduce():
    print("من یک برنامه‌نویسم!")

introduce()


# ------------------------------------------
# ------------------------------------------
# یک دکوراتور بنویس به اسم logger
# که اسم فانکشن رو قبل از اجرا چاپ کنه.
#
# مثال خروجی:
#     [اجرا] add
#     نتیجه: 8
#
# راهنما:
#     - اسم فانکشن توی func.__name__ هست
#     - wrapper باید *args و **kwargs بگیره
#     - فراموش نکن result رو return کنی

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[اجرا] {func.__name__}")
        pass  # کدت اینجا
    return wrapper

@logger
def add(a, b):
    return a + b

print("نتیجه:", add(3, 5))


# ------------------------------------------
# ------------------------------------------
# یک دکوراتور بنویس به اسم timer
# که زمان اجرای فانکشن رو اندازه بگیره و چاپ کنه.
#
# مثال خروجی:
#     زمان اجرا: 1.0008 ثانیه
#
# راهنما:
#     - import time
#     - از time.perf_counter() استفاده کن
#     - تفاضل زمان قبل و بعد = زمان اجرا

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        pass  # کدت اینجا
        end = time.perf_counter()
        print(f"زمان اجرا: {end - start:.4f} ثانیه")
    return wrapper

@timer
def wait():
    time.sleep(1)

wait()


# ------------------------------------------
# ------------------------------------------
# یک دکوراتور بنویس به اسم counter
# که بشماره این فانکشن چند بار صدا زده شده
# و هر بار چاپ کنه.
#
# مثال خروجی:
#     say_hello برای بار 1 اجرا شد
#     say_hello برای بار 2 اجرا شد
#     say_hello برای بار 3 اجرا شد
#
# راهنما:
#     - یک متغیر count = 0 بیرون از wrapper تعریف کن
#     - از nonlocal count داخل wrapper استفاده کن

def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        pass  # کدت اینجا
    return wrapper

@counter
def say_hello():
    pass

say_hello()
say_hello()
say_hello()


# ------------------------------------------
# ------------------------------------------
# دو دکوراتور بنویس:
#     - uppercase: خروجی رو به حروف بزرگ تبدیل کنه
#     - exclaim: یک "!!!" به آخر اضافه کنه
#
# بعد هر دو رو روی یک فانکشن بزار و خروجی رو ببین.
#
# مثال خروجی:
#     HELLO WORLD!!!
#
# راهنما:
#     - ترتیب دکوراتورها مهمه
#     - اول @exclaim بعد @uppercase امتحان کن
#     - بعد برعکسش رو هم امتحان کن و فرق رو ببین

def uppercase(func):
    def wrapper(*args, **kwargs):
        pass  # کدت اینجا
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        pass  # کدت اینجا
    return wrapper

@uppercase
@exclaim
def say_message():
    return "hello world"

print(say_message())


# ------------------------------------------
# ------------------------------------------
# یک دکوراتور بنویس به اسم repeat
# که فانکشن رو N بار اجرا کنه.
# N رو موقع استفاده مشخص می‌کنیم.
#
# مثال خروجی:
#     سلام!
#     سلام!
#     سلام!
#
# راهنما:
#     - repeat یک فانکشن برمی‌گردونه (decorator)
#     - decorator یک فانکشن برمی‌گردونه (wrapper)
#     - wrapper حلقه for داره

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            pass  # کدت اینجا
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("سلام!")

say_hi()