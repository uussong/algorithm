arr = [list(map(int, input().split())) for _ in range(5)]

scores = []
for r in range(5):
    score = 0
    for c in range(4):
        score += arr[r][c]
    scores.append(score)

winner = scores.index(max(scores)) + 1
max_score = max(scores)
print(winner, max_score)