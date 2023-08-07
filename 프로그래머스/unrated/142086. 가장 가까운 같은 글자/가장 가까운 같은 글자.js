function solution(s) {
    const check = {}
    return s.split('').map((item, index) => {
        if(check[item] === undefined) {
            check[item] = index
            return -1
        } else {
            const distance = index - check[item]
            check[item] = index
            return distance
        }
    })
}