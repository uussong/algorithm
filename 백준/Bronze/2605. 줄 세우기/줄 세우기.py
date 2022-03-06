N = int(input())
students = list(map(int, input().split()))
order = []

for i in range(N):
    order.insert(i-students[i], i+1)

print(*order)
