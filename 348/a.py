N = int(input())
for i in range(1, N + 1):
    print("o" if i % 3 != 0 else "x", end="")
