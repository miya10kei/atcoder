N, A, B = map(int, input().split())

cnt = 0
for i in range(1, N + 1):
    s = sum([int(c) for c in str(i)])
    cnt += i if A <= s and s <= B else 0
print(cnt)
