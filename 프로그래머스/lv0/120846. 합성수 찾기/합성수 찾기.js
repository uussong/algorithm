const solution = n => {
    const numbers = new Set()
    for(let i = 1; i <= n; i++) {
        for(let j = 2; j < i; j++) {
            if(i % j === 0) {
                numbers.add(i)
            }
        }
    }

    return numbers.size
}