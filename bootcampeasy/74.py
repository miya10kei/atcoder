A, B, C, X, Y = map(int, input().split())

ans = 0
if (A + B) < C * 2:
    ans = A * X + B * Y
else:
    ans += C * (min(X, Y) * 2)
    if X > Y:
        ans += A * (X - Y)
    elif X < Y:
        ans += B * (Y - X)
print(ans)
