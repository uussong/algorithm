N = int(input())

cute = []
for i in range(N):
    num = int(input())
    cute.append(num)
    
if cute.count(0) > cute.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
