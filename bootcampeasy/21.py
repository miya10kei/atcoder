import sys

X = int(input())

for i in range(X, sys.maxsize):
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                print(i)
                exit(0)
            else:
                break
