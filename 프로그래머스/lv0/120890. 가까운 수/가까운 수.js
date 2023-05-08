function solution(array, n) {
    let answer = 0
    array.sort((a, b) => a - b)
    
    const min = Math.min(...array.map(item => Math.abs(item - n)))
    console.log(min)
    const index = array.map(item => Math.abs(item - n)).indexOf(min)
    const result = array[index]
    return result
}