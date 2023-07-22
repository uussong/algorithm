function solution(t, p) {
    let answer = 0;
    for(let i = 0; i < t.length - p.length + 1; i++) {
        const slicedT = t.slice(i, i + p.length)
        if(Number(slicedT) <= Number(p)) {
            answer += 1
        }
    }
    
    return answer;
}