import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    a, b = input().split()
    # 타이핑 횟수
    cnt = 0
    i = 0

    while i < len(a):
        # b로 타이핑 하는 경우
        if a[i] == b[0]:
            if a[i:i+len(b)] == b:
                # b는 눌러 타이핑했으므로 b의 길이만큼 뒤에서 다음 타이핑함
                i += len(b)
                # 타이핑 횟수 추가
                cnt += 1
            else:
                # b로 타이핑 하지 못 하는 경우 한 글자씩 타이핑
                i += 1
                cnt += 1
        else:
            i += 1
            cnt += 1

    print(f'#{tc} {cnt}')

