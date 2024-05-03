N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))


def calc_temperature(x):
    return 1000 * T - x * 6


ans = -1
diff_min = 100000000
for i in range(N):
    x = calc_temperature(H[i])
    diff = abs(x - A * 1000)
    if diff < diff_min:
        ans = i + 1
        diff_min = diff
print(ans)
