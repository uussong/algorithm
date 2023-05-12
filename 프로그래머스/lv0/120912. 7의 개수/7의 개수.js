function solution(array) {
    let result = 0
    array = array.map(item => item.toString())
    for(const item of array) {
        for(const num of item) {
            if(num === '7') {
                result += 1
            }
        }
    }
    return result
}