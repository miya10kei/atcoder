import itertools
import math

N = int(input())
P = "".join(list(map(str, input().split())))
Q = "".join(list(map(str, input().split())))

s = [x for x in range(1, N + 1)]
c = list(itertools.permutations(s, N))
p = q = 0
for i in range(math.factorial(N)):
    t = "".join(map(str, c[i]))
    if t == P:
        p = i + 1
    if t == Q:
        q = i + 1
print(abs(p - q))
