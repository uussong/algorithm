function solution(arr, divisor) {
    const div = arr.filter(el => el % divisor === 0).sort((a, b) => a - b)
    const answer = div.length > 0 ? div : [-1]
    return answer;
}