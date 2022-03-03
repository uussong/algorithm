T = int(input())
A = 5 * 60
B = 1 * 60
C = 10

if T % 10 != 0:
    print(-1)
else:
    a = b = c = 0
    a = T // A
    b = (T % A) // B
    c = ((T % A) % B) // C

    print(a, b, c)

