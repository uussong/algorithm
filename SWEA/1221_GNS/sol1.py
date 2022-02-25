# import sys
#
# sys.stdin = open('GNS_test_input.txt')
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     n = input()
#     num_list = list(input().split())
#     new_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     sorted_num = []
#
#     for i in range(len(new_num)):
#         for num in num_list:
#             if new_num[i] == num:
#                 sorted_num.append(num)
#     print(f'#{tc}')
#     print(*sorted_num)

import sys

sys.stdin = open('GNS_test_input.txt')

T = int(input())
for t in range(1, T+1):
    N = input()
		#각 개수를 저장하는 딕셔너리
    str_dict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    str_lst = input().split()
    result = ''
    for s in str_lst:
				#각각 카운팅을 해준다.
        str_dict[s] += 1
		#각 원소가 몇개인지 나오기 때문에 앞에서부터 개수만큼 생성한다.
    for key, value in str_dict.items():
        temp = ' '.join([key] * value)
        result += temp + ' '

    print(f'#{t} ')
    print(result[:len(result)-1])