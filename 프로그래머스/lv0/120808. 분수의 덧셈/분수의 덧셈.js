function solution(numer1, denom1, numer2, denom2) {
    var answer = [];

    let GCD = 1;
    let numer = (numer1 * denom2 + numer2 * denom1);
    let denom = (denom1 * denom2);
    
    for (let i = 1; i <= denom1 * denom2; i++){
        if(numer % i === 0 && denom % i === 0) {
            GCD = i
        }
    }

    answer.push(numer / GCD)
    answer.push(denom / GCD)
    return answer;
}

