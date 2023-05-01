const solution = n => {
    let GCD = 1;
    
    for(let i = 1; i <= (6 > n ? n : 6) ; i++){
        if(n % i === 0 && 6 % i === 0) {
            GCD = i
        }
    }
    const LCM = 6 * n / GCD
    const result = LCM / 6
    
    return result
}