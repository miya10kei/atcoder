N, M = map(int, input().split())
PS = [list(input().split()) for _ in range(M)]

wa = [0] * (N + 1)
ac = [False] * (N + 1)
acnum = 0
wanum = 0
for ps in PS:
    n = int(ps[0])
    if not ac[n]:
        if ps[1] == "AC":
            ac[n] = True
            wanum += wa[n]
            acnum += 1
        else:
            wa[n] += 1
print(f"{acnum} {wanum}")
