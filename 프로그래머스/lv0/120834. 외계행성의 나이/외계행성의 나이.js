const solution = age => {
    let answer = ''
    const alphabet = 'abcdefghij'
    age = age.toString()
    for(let i = 0; i < age.length; i++) {
        answer += alphabet[age[i]]
    }
    return answer
}