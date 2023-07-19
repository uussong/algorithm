function solution(s) {
    let answer = '';
    answer = s.split(" ").map(item => item.split('').map((item, idx) => idx % 2 ? item.toLowerCase() : item.toUpperCase()).join('')).join(' ')
    return answer;
}