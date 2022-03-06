import sched


T = int(input())
for _ in range(T):
    N = int(input())
    school = {}
    max_v = 0
    for _ in range(N):
        S, L = input().split()
        L = int(L)
        school[L] = S

    for i in school.keys():
        if i > max_v:
            max_v = i
    print(school[max_v])
    
