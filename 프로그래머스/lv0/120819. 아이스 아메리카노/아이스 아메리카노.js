const solution = money => {
    let answer = []
    answer.push(parseInt(money / 5500), money % 5500)
    return answer
}