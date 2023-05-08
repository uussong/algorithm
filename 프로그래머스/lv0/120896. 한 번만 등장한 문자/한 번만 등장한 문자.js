function solution(s) {
    let result = []
    const count = {}
    for(const item of s) {
        if (count[item]) {
            count[item] += 1
        } else {
            count[item] = 1
        }
    }
    for(const item in count) {
        if (count[item] === 1) {
            result.push(item)
        }
    }
    result.sort()
    return result.join('')
}