N = int(input())
a = list(map(int, input().split()))

answer = sum(i - 1 for i in a)

print(answer)
