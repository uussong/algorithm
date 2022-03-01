T = int(input())

for _ in range(T):
    formula = list(map(str, input().split()))
    R = float(formula[0])

    for i in range(1, len(formula)):
        if formula[i] == '@':
            R *= 3
        elif formula[i] == '%':
            R += 5
        elif formula[i] == '#':
            R -= 7
    print(f'{R:.2f}')
