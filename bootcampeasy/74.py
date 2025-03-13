A, B, C, X, Y = map(int, input().split())

answer = 0
if (A + B) < C * 2:
    answer = A * X + B * Y
else:
    answer += C * (min(X, Y) * 2)
    if X > Y:
        answer += min(A * (X - Y), 2 * C * (X - Y))
    elif X < Y:
        answer += min(B * (Y - X), 2 * C * (Y - X))
print(answer)
