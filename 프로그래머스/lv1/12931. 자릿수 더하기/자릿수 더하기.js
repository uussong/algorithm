function solution(n){
    return n.toString().split('').reduce((acc, cur) => parseInt(cur) + acc, 0)
}