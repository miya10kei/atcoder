N = int(input())
D = list(map(int, input().split()))

D.sort()
m = int(N / 2)
print(D[m] - D[m - 1])
