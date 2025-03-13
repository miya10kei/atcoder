N = int(input())
a = list(int(input()) for _ in range(N))

cur = 1
answer = 0
visited = {1}
while cur != 2:
    cur = a[cur - 1]
    if cur in visited:
        answer = -1
        break
    visited.add(cur)
    answer += 1
print(answer)
