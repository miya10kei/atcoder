import math

a, b = map(int, input().split())
s = int(f"{a}{b}")
sqrt = math.sqrt(s)
print("Yes" if sqrt == round(sqrt) else "No")
