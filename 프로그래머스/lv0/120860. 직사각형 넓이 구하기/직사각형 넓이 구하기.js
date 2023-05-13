function solution(dots) {
    let result = 0
    const x = []
    const y = []
    dots.forEach(dot => {
        dot.forEach((item, index) => {
            if (index % 2) {
                y.push(item)
            } else {
                x.push(item)
            }
        })
    })
    x.sort((a, b) => a - b)
    y.sort((a, b) => a - b)
    result = (x[3] - x[0]) * (y[3] - y[0])
    return result
}