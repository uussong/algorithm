function solution(numbers) {
    const noNumbers = []
    for (let i = 0; i < 10; i++) {
        if (!numbers.includes(i)) {
            noNumbers.push(i)
        }
    }
    return noNumbers.reduce((a, b) => a + b, 0)
}