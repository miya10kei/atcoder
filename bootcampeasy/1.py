import math

A, B = map(int, input().split())
print(int(math.ceil((B - A) / (A - 1)) + 1))
