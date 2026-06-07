# =========================
# Python Dictionary Cheatsheet
# =========================

print("========== DICTIONARY ==========\n")

# -------------------------
# Dictionary Creation
# -------------------------

user = {
    "name": "Alice",
    "age": 27,
    "score": 91.5,
}

print("Dictionary:")
print(user)

# -------------------------
# Accessing Values
# -------------------------

print("\nAccess:")

print(user["name"])
print(user["age"])

# safer access
print(user.get("score"))

# اگر وجود نداشته باشد:
print(user.get("city"))          # None
print(user.get("city", "N/A"))  # default value

# -------------------------
# Add / Update
# -------------------------

print("\nAdd / Update:")

user["city"] = "Berlin"

print(user)

user["age"] = 30

print(user)

# -------------------------
# Remove
# -------------------------

print("\nRemove:")

del user["score"]

print(user)

removed = user.pop("city")

print("Removed:", removed)
print(user)

# -------------------------
# Iteration
# -------------------------

print("\nIteration:")

for key in user:
    print(key)

print()

for value in user.values():
    print(value)

print()

for key, value in user.items():
    print(f"{key:<10} => {value}")

# -------------------------
# Membership
# -------------------------

print("\nMembership:")

print("name" in user)
print("salary" in user)

# -------------------------
# Dictionary Comprehension
# -------------------------

print("\nDictionary Comprehension:")

squares = {x: x * x for x in range(5)}

print(squares)

# -------------------------
# Nested Dictionary
# -------------------------

print("\nNested Dictionary:")

users = {
    1: {
        "name": "Alice",
        "age": 27,
    },
    2: {
        "name": "Bob",
        "age": 31,
    }
}

print(users)

print(users[1]["name"])

# -------------------------
# Common Methods
# -------------------------

print("\nMethods:")

print("Keys:", user.keys())
print("Values:", user.values())
print("Items:", user.items())

# copy
copy_user = user.copy()

print("\nCopy:")
print(copy_user)

# update
user.update({
    "country": "Germany",
    "vip": True,
})

print("\nAfter update:")
print(user)

# -------------------------
# setdefault
# -------------------------

print("\nsetdefault:")

user.setdefault("language", "Python")

print(user)

# اگر وجود داشته باشد تغییر نمی‌دهد
user.setdefault("name", "Changed")

print(user)

# -------------------------
# Frequency Counter Example
# -------------------------

print("\nFrequency Counter:")

text = "banana"

counter = {}

for ch in text:
    counter[ch] = counter.get(ch, 0) + 1

print(counter)

# -------------------------
# Sorting Dictionary
# -------------------------

print("\nSorting:")

scores = {
    "Alice": 90,
    "Bob": 75,
    "Charlie": 95,
}

sorted_items = sorted(scores.items(), key=lambda x: x[1])

print(sorted_items)

# -------------------------
# Why Dictionary?
# -------------------------

print("\nDictionary Advantages:")
print("- Key-Value storage")
print("- Very fast lookup")
print("- Hash table based")
print("- Flexible structure")
print("- Great for indexing/cache")

# -------------------------
# Performance Idea
# -------------------------

print("\nComplexity:")

print("dict lookup:")




# XIPPPP
# ساخت dictionary با zip و loop

keys = ["name", "age", "city"]
values = ["Alice", 27, "Berlin"]

# -------------------------
# Method 1: dict + zip
# -------------------------

user = dict(zip(keys, values))

print(user)

# خروجی:
# {'name': 'Alice', 'age': 27, 'city': 'Berlin'}


# -------------------------
# Method 2: for loop
# -------------------------

user2 = {}

for key, value in zip(keys, values):
    user2[key] = value

print(user2)


# -------------------------
# مشاهده zip
# -------------------------

z = zip(keys, values)

print(list(z))

# خروجی:
# [('name', 'Alice'), ('age', 27), ('city', 'Berlin')]


# -------------------------
# Dictionary Comprehension
# -------------------------

user3 = {
    key: value
    for key, value in zip(keys, values)
}

print(user3)


# =========================================================
# Example: combine two lists into mapping
# =========================================================

products = ["iphone", "macbook", "ipad"]
prices = [999, 2499, 799]

price_map = dict(zip(products, prices))

print(price_map)


# =========================================================
# enumerate + dict
# =========================================================

names = ["alice", "bob", "charlie"]

indexed = dict(enumerate(names))

print(indexed)

# خروجی:
# {0: 'alice', 1: 'bob', 2: 'charlie'}