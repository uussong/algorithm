const solution = my_string => {
    let answer = ''
    for (let str of my_string) {
        str === str.toUpperCase() ? answer += str.toLowerCase() : answer += str.toUpperCase()
    }
    return answer
}