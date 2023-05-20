function solution(i, j, k) {
    let result = 0
    const num = []
    for(let n = i; n <= j; n++) {
        num.push(...n.toString().split(''))
    }
    num.forEach(item => {
        if (item == k) {
            result += 1
        }
    })
    return result
}