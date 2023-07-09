function solution(a, b) {
    let answer = '';
    const date = new Date(2016, a - 1, b);
    answer = date.toDateString().slice(0, 3).toUpperCase()
    return answer;
}