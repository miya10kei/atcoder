import math

dishes = [int(input()) for _ in range(5)]


def rollup(x):
    return int(math.floor((x + 9) / 10) * 10)


max = 0
index = 0
for i in range(5):
    diff = rollup(dishes[i]) - dishes[i]
    if diff > max:
        max = diff
        index = i

ans = 0
for i in range(5):
    ans += dishes[i] if i == index else rollup(dishes[i])
print(ans)
