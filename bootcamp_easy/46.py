A, B, C, K = map(int, input().split())

ans = A - B

if ans > pow(10, 18):
    print("Unfair")
print(ans if K % 2 == 0 else -ans)
