import sys

N, M = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: x[0])

amount = 0
answer = 0
for ab in AB:
    for i in range(1, ab[1] + 1):
        answer += ab[0]
        amount += 1
        if amount == M:
            print(answer)
            sys.exit()
