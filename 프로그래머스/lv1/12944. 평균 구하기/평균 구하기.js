function solution(arr) {
    let answer = 0;
    const length = arr.length;
    
    answer = arr.reduce((acc, cur) => acc + cur) / length;
    return answer;
}