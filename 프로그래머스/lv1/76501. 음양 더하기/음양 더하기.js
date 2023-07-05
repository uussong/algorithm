function solution(absolutes, signs) {
    signs = signs.map(el => el === true ? 1 : -1)
    const multiply = []
    for(let i = 0; i < absolutes.length; i++) {
        multiply.push(absolutes[i] * signs[i])
    }
    const answer = multiply.reduce((a, b) => a + b, 0)
    return answer
}