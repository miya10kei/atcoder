N = int(input())
X = list(map(int, input().split()))

X.sort()
s = {}
for i in range(X[0], X[-1] + 1):
    s[i] = 0
    for x in X:
        s[i] += pow(x - i, 2)
print(min(s.values()))
