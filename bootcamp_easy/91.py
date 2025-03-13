import itertools
import math

<<<<<<< HEAD
N = int(input())
=======
N = int(input())
indices = list(range(N))
>>>>>>> Snippet
xy = [list(map(int, input().split())) for _ in range(N)]

distances = []
for p in itertools.permutations(list(range(N)), N):
    distance = 0
    for i in range(N - 1):
        pre = p[i]
        next = p[i + 1]
        distance += math.sqrt(pow(xy[pre][0] - xy[next][0], 2) + pow(xy[pre][1] - xy[next][1], 2))
    distances.append(distance)

answer = sum(distances) / len(distances)
print(answer)
