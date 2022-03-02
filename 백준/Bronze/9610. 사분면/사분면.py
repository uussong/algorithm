n = int(input())
cnt1 = cnt2 = cnt3 = cnt4 = cnt5 = 0
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        cnt1 += 1

    elif x < 0 and y > 0:
        cnt2 += 1
        
    elif x < 0 and y < 0:
        cnt3 += 1
        
    elif x > 0 and y < 0:
        cnt4 += 1
        
    elif x == 0 or y == 0:
        cnt5 += 1
        

print(f'Q1: {cnt1}')
print(f'Q2: {cnt2}')
print(f'Q3: {cnt3}')
print(f'Q4: {cnt4}')
print(f'AXIS: {cnt5}')