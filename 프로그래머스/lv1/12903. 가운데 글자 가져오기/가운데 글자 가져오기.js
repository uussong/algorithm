function solution(s) {
    let answer = '';
    if (s.length % 2 !== 0) {
        answer = s[Math.floor(s.length / 2)]
    } else {
         answer = s[Math.floor(s.length / 2) - 1] + s[Math.floor(s.length / 2)]
    }
    return answer;
}