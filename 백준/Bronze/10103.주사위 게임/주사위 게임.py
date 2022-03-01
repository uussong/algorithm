n = int(input())

score1 = score2 = 100
for _ in range(n):
    num1, num2 = map(int, input().split())
    if num1 > num2:
        score2 -= num1
    elif num1 < num2:
        score1 -= num2
    
print(score1) 
print(score2)
