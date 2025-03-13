N = int(input())
a = list(map(int, input().split()))

answer = 0
for i in range(1, N + 1):
    answer += int(i == a[a[i - 1] - 1])

answer /= 2
print(int(answer))
