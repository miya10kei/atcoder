import math

N = int(input())
X = int(N / 1.08)

if N == int(math.floor(X * 1.08)):
    print(X)
elif N == int(math.floor((X + 1) * 1.08)):
    print(X + 1)
elif N == int(math.floor((X - 1) * 1.08)):
    print(X - 1)
else:
    print(":(")
