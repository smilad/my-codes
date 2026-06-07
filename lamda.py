# =========================
# Python Lambda Functions
# =========================

# A lambda function is a small anonymous function
# (without a name) used for simple operations.

# Syntax:
# lambda arguments: expression

# -------------------------
# 1) Basic lambda
# -------------------------

add = lambda a, b: a + b

print(add(2, 3))  # 5


# -------------------------
# 2) lambda vs def
# -------------------------

def add_def(a, b):
    return a + b

# same as:
add_lambda = lambda a, b: a + b


# -------------------------
# 3) use with map
# -------------------------

nums = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, nums))

print(squared)  # [1, 4, 9, 16]


# -------------------------
# 4) use with filter
# -------------------------

nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)  # [2, 4, 6]


# -------------------------
# 5) lambda in sorting
# -------------------------

pairs = [(1, 3), (2, 1), (5, 2)]

sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # [(2, 1), (5, 2), (1, 3)]


# -------------------------
# 6) IMPORTANT RULES
# -------------------------

# lambda:
# - only one expression
# - no statements (no for, while, if block)
# - returns automatically

# good for:
# - map
# - filter
# - sorted
# - small inline functions

# bad for:
# - complex logic
# - multi-step operations