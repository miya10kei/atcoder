X, Y = map(int, input().split())

answer = 0
while X <= Y:
    X *= 2
    answer += 1

print(answer)
