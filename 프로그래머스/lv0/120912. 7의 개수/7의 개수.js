function solution(array) {
    let result = 0
    array = array.map(item => item.toString())
    result = array.join('').match(/7/g)
    if (result === null) {
        return 0
    }
    return result.length
}