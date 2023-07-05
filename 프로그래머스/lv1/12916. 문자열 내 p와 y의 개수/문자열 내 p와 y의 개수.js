function solution(s){
    const p = s.toLowerCase().split('').filter(el => el === 'p')
    const y = s.toLowerCase().split('').filter(el => el === 'y')
    const answer = p.length === y.length ? true : false
    return answer
}