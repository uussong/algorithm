function solution(polynomial) {
    const x = []
    const number = []
    polynomial
    .split(' ')
    .forEach(item => {
        item.match(/.x|x$/g) ? x.push(item) : item !== '+' ? number.push(parseInt(item)) : null
    })
    
    let numX = x
                .map(item => item === 'x' ? item = 1 : item = parseInt(item))
                .reduce((a, b) => a + b, 0)
    let sum = number.reduce((a, b) => a + b, 0)

    if (numX && sum) {
        if (numX === 1) {
            return `x + ${sum}`
        }
        return `${numX}x + ${sum}`
    }
    if (numX && !sum) {
        if (numX === 1) {
            return `x`
        }
        return `${numX}x`
    }
    if (!numX) return `${sum}`
}