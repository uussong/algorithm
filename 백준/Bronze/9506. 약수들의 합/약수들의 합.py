while True:
    n = int(input())

    if n == -1:
        break
    
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    
    if sum(divisor) == n:
        ans = str(n) + ' = ' + '1'
        for j in range(1, len(divisor)):
            ans += ' + ' + str(divisor[j])
        
        print(ans)
    else:
        print(str(n) + ' is NOT perfect.')