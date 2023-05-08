const solution = (cipher, code) => {
    let answer = ''
    cipher = cipher.split('')
    for(let i = code - 1; i < cipher.length; i += code) {
        answer += cipher[i]
    }
    return answer
}