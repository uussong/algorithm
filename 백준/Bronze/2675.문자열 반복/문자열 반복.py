T = int(input())

for _ in range(T):
    R, S = input().split()
    P = ''
    for i in S:
        P += int(R) * i
    print(P)