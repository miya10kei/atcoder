H, W = map(int, input().split())
A = [input() for _ in range(H)]

print("#" * (W + 2))
for a in A:
    print(f"#{a}#")
print("#" * (W + 2))
