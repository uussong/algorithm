function solution(my_string) {
    const number = my_string.match(/[0-9]+/g)
    return number ? number.map(item => parseInt(item)).reduce((a, b) => a + b, 0) : 0
}