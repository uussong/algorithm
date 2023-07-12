function solution(sizes) {
    let answer = 0;
    sizes.forEach(size => size.sort((a, b) => a - b))
    const left = sizes.map(item => item[0])
    const right = sizes.map(item => item[1])
    answer = Math.max(...left) * Math.max(...right)
    return answer
}