const solution = num_list => {
    let answer = []
    num_list.forEach(num => answer.unshift(num))
    return answer
}