N = int(input())
K = int(input())
X = list(map(int, input().split()))

ans = 0
for x in X:
    a = x
    ans += min(a, abs(x - K)) * 2
print(ans)
