const solution = hp => {
    let answer = 0
    if (hp / 5) {
        answer += parseInt(hp / 5)
        hp %= 5
        if (hp / 3) {
            answer += parseInt(hp / 3)
            hp %= 3
        } 
        answer += hp
    }  
    return answer
}