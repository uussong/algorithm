import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    #버블 정렬로 오름차순 정렬
    for j in range(len(num_list)):
        for i in range(len(num_list)-1):
            if num_list[i] > num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

    # 뒤에서 하나 앞에서 하나씩 교차로 값 추가
    new_sort = []
    for i in range(5):
        new_sort.append(num_list[-1-i])
        new_sort.append(num_list[i])

    # 각각의 값을 리스트에서 빼서 출력
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(new_sort[i], end=' ')
    print()


