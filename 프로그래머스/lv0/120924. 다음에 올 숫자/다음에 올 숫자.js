function solution(common) {
    let result
    if(common[0] + common[2] === 2 * common[1]) {
        difference = common[1] - common[0]
        result = common[common.length - 1] + difference
    } else {
        difference = common[1] / common[0]
        result = common[common.length - 1] * difference
    }
    return result
}