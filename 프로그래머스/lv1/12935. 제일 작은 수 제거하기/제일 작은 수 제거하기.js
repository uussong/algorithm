function solution(arr) {
    if (arr.length === 1) return [-1]
    const sortedArr = [...arr].sort((a, b) => a - b)
    const smallestNumber = sortedArr[0]
    return arr.filter(num => num !== smallestNumber)
}