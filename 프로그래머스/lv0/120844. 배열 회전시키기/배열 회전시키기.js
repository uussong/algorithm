const solution = (numbers, direction) => {
    if (direction === 'right') {
        const last = numbers.pop()
        numbers.unshift(last)
        return numbers
    } else {
        const first = numbers.shift()
        numbers.push(first)
        return numbers
    }
}