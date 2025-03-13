N = int(input())
A = [int(input()) for _ in range(N)]
_A = sorted(A, reverse=True)

for i in range(N):
    print(_A[1] if _A[0] == A[i] else _A[0])
