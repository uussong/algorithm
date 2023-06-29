function solution(n) {
    return n.toString().split("").reverse().map(s => parseInt(s))
}