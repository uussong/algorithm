function solution(x) {
    const digitSum = x.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b), 0)
    const isHarshad = x % digitSum === 0
    return isHarshad
}