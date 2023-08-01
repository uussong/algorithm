function solution(name, yearning, photo) {
    const score = {}
    for (let i = 0; i < name.length; i++) {
        score[name[i]] = yearning[i]
    }
    const answer = photo.map(item => item.reduce((acc, cur) => acc + (score[cur] ? score[cur] : 0), 0))
    return answer;
}