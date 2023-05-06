const solution = my_string => {
    let answer = []
    for(let i = 0; i < my_string.length; i++) {
         !isNaN(parseInt(my_string[i])) ? answer.push(parseInt(my_string[i])) : null
    }
    answer.sort((a, b) => a - b)
    return answer
}