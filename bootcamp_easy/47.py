N = int(input())

L = [] * 5
L.append(2)
L.append(1)

if N <= 1:
    print(L[N])
    exit(0)

for i in range(2, N + 1):
    L.append(L[i - 2] + L[i - 1])
print(L[-1])
