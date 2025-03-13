N, K = list(map(int, input().split()))

answer = K * (K - 1) ** (N - 1)
print(answer)
