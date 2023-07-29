function solution(s) {
    let answer = '';
    numbers = s.split(' ').map(item => Number(item)).sort((a, b) => a - b)
    answer = `${numbers[0]} ${numbers[numbers.length - 1]}`
    return answer;
}