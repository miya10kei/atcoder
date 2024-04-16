S, T = input().split()

is_s_plus = False
if S.startswith("B"):
    s = -int(S[1])
else:
    s = int(S[0])
    is_s_plus = True

is_t_plus = False
if T.startswith("B"):
    t = -int(T[1])
else:
    t = int(T[0])
    is_t_plus = True

print(abs(t - s) - (1 if is_s_plus != is_t_plus else 0))
