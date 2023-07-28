function solution(n) {
    let answer = 0;
    answer = Number.isInteger(Math.sqrt(n)) ? (Math.sqrt(n) + 1) ** 2 : -1
    return answer
}