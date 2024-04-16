S = input().upper()
T = input()


def check(S, T):
    i = 0

    for t in T:
        while i < len(S) and S[i] != t:
            i += 1
        if i == len(S):
            return False
        i += 1
    return True


print("Yes" if check(S, T[:-1] if T.endswith("X") else T) else "No")
