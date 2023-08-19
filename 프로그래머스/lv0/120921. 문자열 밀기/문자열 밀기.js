function solution(A, B) {
    if (A === B) return 0
    
    let answer = -1
    B = B + B
    return B.indexOf(A)
}