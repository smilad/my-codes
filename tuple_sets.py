# =========================
# Python Tuple & Set Cheatsheet
# =========================

print("========== TUPLE ==========\n")

# -------------------------
# Tuple Creation
# -------------------------

t1 = (1, 2, 3)
print("Tuple:", t1)

# تک عضو باید comma داشته باشد
single = (5,)
print("Single tuple:", single)

# بدون پرانتز هم می‌شود
t2 = 10, 20, 30
print("Tuple without ():", t2)

# -------------------------
# Accessing
# -------------------------

print("\nFirst item:", t1[0])
print("Last item:", t1[-1])

# slicing
print("Slice:", t1[0:2])

# -------------------------
# Immutable
# -------------------------

print("\nTuple is immutable")

# این خط error می‌دهد:
# t1[0] = 100

# -------------------------
# Packing / Unpacking
# -------------------------

point = (4, 7)

x, y = point

print("\nUnpacking:")
print("x =", x)
print("y =", y)

# swap بدون temp variable
a = 10
b = 20

a, b = b, a

print("\nSwap:")
print("a =", a)
print("b =", b)

# -------------------------
# Tuple Methods
# -------------------------

nums = (1, 2, 3, 2, 2)

print("\ncount:", nums.count(2))
print("index:", nums.index(3))

# -------------------------
# Why Tuple?
# -------------------------

print("\nTuple Advantages:")
print("- Immutable")
print("- Faster than list")
print("- Hashable (can be dict key)")
print("- Good for fixed data")

# tuple as dict key
locations = {
    (35.7, 51.4): "Tehran",
    (48.8, 2.3): "Paris",
}

print("\nTuple as dict key:")
print(locations[(35.7, 51.4)])


# ============================================================
# SET
# ============================================================

print("\n\n========== SET ==========\n")

# -------------------------
# Set Creation
# -------------------------

s1 = {1, 2, 3, 4}

print("Set:", s1)

# تکراری حذف می‌شود
s2 = {1, 1, 1, 2, 2, 3}

print("Duplicates removed:", s2)

# set خالی
empty = set()

print("Empty set:", empty)

# -------------------------
# Add / Remove
# -------------------------

s1.add(5)

print("\nAfter add:", s1)

s1.remove(3)

print("After remove:", s1)

# discard error نمی‌دهد
s1.discard(100)

print("After discard:", s1)

# -------------------------
# Membership O(1)
# -------------------------

print("\nMembership:")

print(2 in s1)
print(100 in s1)

# -------------------------
# Set Operations
# -------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\nA:", a)
print("B:", b)

# union
print("\nUnion:", a | b)

# intersection
print("Intersection:", a & b)

# difference
print("Difference A-B:", a - b)

# symmetric difference
print("Symmetric Difference:", a ^ b)

# -------------------------
# Useful Trick
# -------------------------

nums = [1, 2, 2, 3, 3, 3, 4]

unique = list(set(nums))

print("\nRemove duplicates:")
print(unique)

# -------------------------
# Set Comprehension
# -------------------------

squares = {x * x for x in range(5)}

print("\nSet comprehension:")
print(squares)

# -------------------------
# Frozen Set
# -------------------------

fs = frozenset([1, 2, 3])

print("\nFrozen set:", fs)

# immutable set
# fs.add(4) => error

# -------------------------
# Why Set?
# -------------------------

print("\nSet Advantages:")
print("- Fast lookup O(1)")
print("- Unique values")
print("- Mathematical operations")
print("- Great for deduplication")