function solution(score) {
    const result = []
    const sum = score.map(item => item.reduce((a, b) => a + b), 0)
    const rank = [...sum].sort((a, b) => b - a)
    for(let i = 0; i < sum.length; i++) {
        result.push((rank.indexOf(sum[i]) + 1) )
    }
    return result
}