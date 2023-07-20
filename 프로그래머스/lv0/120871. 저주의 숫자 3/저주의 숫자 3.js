function solution(n) {
    let answer = 0;
    let count = 0
    for(let i = 1; i <= n + count; i++) {
        answer += 1
        if (i % 3 === 0 || i.toString().includes(3)) {
            count += 1
        }
    }
    
    return answer;
}