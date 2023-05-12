function solution(my_string) {
    const calculate = my_string.split(' ')
    let result = parseInt(calculate[0])
    calculate.forEach((item, index) => {
        if (item === '+') {
            result += parseInt(calculate[index + 1])
        } else if (item === '-') {
            result -= parseInt(calculate[index + 1])
        }
    })
    return result
}