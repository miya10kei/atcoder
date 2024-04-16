import math

N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]

for coord in coords:
    max = 0
    ans = 0
    for i, _coord in enumerate(coords):
        d = math.sqrt(pow((coord[0] - _coord[0]), 2) + pow((coord[1] - _coord[1]), 2))
        if d > max:
            max = d
            ans = i + 1
    print(ans)
