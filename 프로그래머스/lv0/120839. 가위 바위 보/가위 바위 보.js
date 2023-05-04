const solution = rsp => {
    let answer = ''
    for(let i of rsp) {
        i === '0' ? answer += '5' : i === '2' ? answer += '0' : answer += '2'
    }
    return answer
}