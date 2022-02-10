import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    cnt = int(input()) # 빌딩 수
    buildings = list(map(int, input().split())) # 빌딩 목록
    ans = 0 # 조망권이 확보된 세대

    for i in range(2, cnt-2):
        curr_height = buildings[i]
        
        if not curr_height: # 빌딩이 안 지어진 곳이라면
            continue

        else: # continue 되니까 자동으로 else가 되어 안 적어주기도 함
            max_height = 0 # 이번 빌딩을 기준으로 한 양 옆 빌딩들 중 가장 높은 높이

            # 양 옆 두 칸씩의 빌딩 높이를 구하기
            d_col = [-2, -1, 1, 2]
            for d in d_col:
                check_idx = i + d # 양 옆 두 칸 빌딩의 idx
                if buildings[check_idx] > max_height:
                    max_height = buildings[check_idx] # 최대 높이 갱신

            if curr_height > max_height: # 조망권이 확보된 경우
                ans += curr_height - max_height

    print(f'#{tc} {ans}')

