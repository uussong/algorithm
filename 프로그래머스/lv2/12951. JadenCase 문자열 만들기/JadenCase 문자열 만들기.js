function solution(s) {
    const answer = s.toLowerCase().split(' ').map(item => item.replace(item[0], (i, idx) => (isNaN(i) || idx === 0) ? i.toUpperCase() : i)).join(' ')
    return answer;
}