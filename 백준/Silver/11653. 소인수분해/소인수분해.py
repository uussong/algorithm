N = int(input())

for i in range(2, N+1):
    while True:
        if N % i:
            break
        if N // i and N % i == 0:
            print(i)
            N = N // i
        
