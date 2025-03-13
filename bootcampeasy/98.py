A, B, C = list(map(int, input().split()))

if A * B * C % 2 == 0:
    answer = 0
else:
    answer = min(A * B, A * C, B * C)
print(answer)
