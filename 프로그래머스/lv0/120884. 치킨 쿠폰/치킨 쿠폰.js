function solution(chicken) {
    let result = 0
    let rest = 0
    while (chicken >= 1) {
        result += parseInt(chicken / 10)
        rest += chicken % 10
        chicken = chicken / 10
    }
    result += parseInt(rest / 10)
    return result
}