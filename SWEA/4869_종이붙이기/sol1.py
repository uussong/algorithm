import sys

sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    paper = [1, 3] # 연산에 활용할 N=10, 20일 때 값 저장
    # N은 10의 배수 / N = 30, i = 2 / N = 40, i = 3 ... 등으로 활용하기 위해  몫을 취함
    for i in range(2, N//10):
        paper.append(paper[i-1] + paper[i-2] * 2) # 규칙에 따라 연산

    print(f'#{tc} {paper[-1]}') # N에서 가능한 영역의 개수는 paper의 마지막 요소

