function solution(s) {
    let answer = 0;
    const numberList = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    const wordNumbers = Object.keys(numberList)
    const numbers = Object.values(numberList)
    
    wordNumbers.forEach((word, index) => {
        const reg = new RegExp(word, 'gi')
        s = s.replace(reg, numbers[index])
    })
    answer = Number(s)
    return answer;
}