function solution(n, m) {
    let GCD = 0
    
    for(let i = 1; i <= Math.min(n, m); i++) {
        if(n % i === 0 && m % i === 0) {
            GCD = i
        }
    }

    const answer = [GCD, n * m / GCD]
    return answer;
}