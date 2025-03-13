N, M, X = map(int, input().split())
A = list(map(int, input().split()))

M = [0] * (N + 1)
for a in A:
    M[a] = 1
print(min(sum(M[0:X]), sum(M[X:])))
