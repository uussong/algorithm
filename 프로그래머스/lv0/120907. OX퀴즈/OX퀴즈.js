function solution(quiz) {
    const result = []
    quiz.forEach((exp) => {
        exp = exp.split(' ')
        let answer = parseInt(exp[0])
        exp.forEach((item, index) => {
            if(item === '+') {
                answer += parseInt(exp[index + 1])
            } else if (item === '-') {
                answer -= parseInt(exp[index + 1])
            }
        })
        if (parseInt(exp[exp.length - 1]) === answer) {
            result.push('O')
        } else {
            result.push('X')
        }
        
    })
    
    
    return result
}