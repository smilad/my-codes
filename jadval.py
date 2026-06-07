n = 10

print("    ", end="")
for j in range(1, n + 1):
    print(f"{j:4}", end="")
print()

print("   " + "-" * (4 * n))

for i in range(1, n + 1):
    print(f"{i:2} |", end="")

    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")

    print()