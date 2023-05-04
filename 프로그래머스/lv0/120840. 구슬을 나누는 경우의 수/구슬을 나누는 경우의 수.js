function solution(balls, share) {
    let answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return Math.round(answer)
}

function factorial(n) {
    let result = 1
    for(let i = 2; i <= n; i++) {
        result *= i
    }
    return result
}
