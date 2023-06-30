function solution(a, b) {
    if (a > b) {
        [a, b] = [b, a]
    }
    let answer = 0
    for (let i = a; i <= b; i++) {
        answer += i
    }
    return answer;
}