K, N, M = map(int, input().split())
total = K * N
rlt = 0

if total > M:
    rlt = total - M

print(rlt)  