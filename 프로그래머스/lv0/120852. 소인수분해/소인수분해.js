function solution(n) {
    const answer = new Set()
    let i = 2
    while(i <= n) {
        if(n % i === 0) {
            n = n / i
            answer.add(i)
        } else {
            i++
        }
        
    }
    const result = [...answer]
    return result
}