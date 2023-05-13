const solution = (array, height) => {
    let answer = 0
    array.forEach(item => item > height ? answer++ : answer)
    return answer
}