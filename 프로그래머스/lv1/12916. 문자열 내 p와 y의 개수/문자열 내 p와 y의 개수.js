function solution(s){
    p = s.toLowerCase().split('').filter(el => el === 'p')
    y = s.toLowerCase().split('').filter(el => el === 'y')
    answer = p.length === y.length ? true : false
    return answer
}