N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

s = [K - Q] * N
for i in A:
    s[i - 1] += 1
for i in range(len(s)):
    print("Yes" if s[i] > 0 else "No")
