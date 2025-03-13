N = int(input())
S = input()

ans = 0
cnt = 0
for s in S:
    if s == "I":
        cnt += 1
    elif s == "D":
        cnt -= 1
    ans = max(ans, cnt)
print(ans)
