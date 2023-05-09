const solution = array => {
    let answer = []
    let maxValue = 0
    array.forEach((value, index) => {
        if(value > maxValue) {
            answer = [value, index]
            maxValue = value
        }
    })
   
    return answer
}