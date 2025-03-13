import itertools

A, B, C, D = list(input())

operators = ["+", "-"]

for op123 in itertools.product(operators, repeat=3):
    expr = f"{A}{op123[0]}{B}{op123[1]}{C}{op123[2]}{D}"
    if eval(expr) == 7:
        print(f"{expr}=7")
        break
