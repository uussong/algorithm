N, K = map(int, input().split())
divisor = []
for i in range(1, N+1):
    if N%i == 0:
        divisor.append(i)

if len(divisor) >= K:
    print(divisor[K-1])
else:
    print(0)