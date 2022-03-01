A, B = map(int, input().split())
C = int(input())

M = B + C

if M >= 60:
    A += M // 60
    M = M % 60
    if A >= 24:
        A = A % 24

print(A, M)