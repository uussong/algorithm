function solution(a, b) {
    let GCD = 0
    for (let i = 1; i <= b; i++) {
        if (a % i === 0 && b % i === 0) GCD = i
    }
    b = b / GCD
    
    while (b % 2 === 0) b = b / 2
    while (b % 5 === 0) b = b / 5
    return b === 1 ? 1 : 2
}