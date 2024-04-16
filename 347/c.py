N, A, B = map(int, input().split())
D = list(map(int, input().split()))

w = A + B
d = []
for i in range(N):
    d.append(D[i] % w)

d.sort()

for i in range(N):
    d.append(d[i] + w)

for i in range(len(d) - 1):
    if d[i + 1] - d[i] > B:
        print("Yes")
        exit(0)
print("No")
