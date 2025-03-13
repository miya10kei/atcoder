A, B, C = map(int, input().split())

ans = 0
if A == B and B == C:
    if A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        ans = -1
else:
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        _A = A
        A = (A + B) / 2
        B = (B + C) / 2
        C = (C + _A) / 2
        ans += 1
print(ans)
