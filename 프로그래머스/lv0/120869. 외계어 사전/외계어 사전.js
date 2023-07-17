function solution(spell, dic) {
    let answer = 0;
    
    for (let i = 0; i < dic.length; i++) {
        let notInclude = 0
        for (let j = 0; j < spell.length; j++) {
            if(dic[i].indexOf(spell[j]) === -1) {
                notInclude++
            }
        }
        notInclude ? answer = 2 : answer = 1
        notIclude = 0
        if (answer === 1) break
    }
    return answer;
}