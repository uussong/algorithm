function solution(s, n) {
    const answer = s.split('').map(i => {
        const char = i.charCodeAt()
        if (char >= 65 && char <= 90) {
            return String.fromCharCode((char - 65 + n) % 26 + 65)
        } else if (char >= 97 && char <= 122) {
            return String.fromCharCode((char - 97 + n) % 26 + 97)
        }
        return ' '
    }).join('')
    return answer;
}