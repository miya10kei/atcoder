x1, y1, x2, y2 = map(int, input().split())

dx21 = x2 - x1
dy21 = y2 - y1

x3 = x2 - dy21
y3 = y2 + dx21

dx32 = x3 - x2
dy32 = y3 - y2
x4 = x3 - dy32
y4 = y3 + dx32

print(f"{x3} {y3} {x4} {y4}")
