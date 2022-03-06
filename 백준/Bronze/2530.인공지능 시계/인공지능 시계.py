A, B, C = map(int, input().split())
D = int(input())

S = (C + D) % 60
M = (B + (C + D) // 60) % 60
H = (A + (B + (C + D) // 60) // 60) % 24
print(H, M, S)