function solution(num, total) {
    let answer = [];
    const mid = parseInt(total / num)
    const half = parseInt(num / 2)
    if(num % 2) {
        for (let i = mid - half; i <= mid + half; i++) {
            answer.push(i)
        }
    } else {
        for (let i = mid - (half - 1); i <= mid + half; i++) {
            answer.push(i)
        }
    }
    return answer;
}