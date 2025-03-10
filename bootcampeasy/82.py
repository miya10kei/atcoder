Q, H, S, D = map(int, input().split())
N = int(input())

ans = N // 2 * min(8 * Q, 4 * H, 2 * S, D)
ans += N % 2 * min(4 * Q, 2 * H, S)
print(ans)
