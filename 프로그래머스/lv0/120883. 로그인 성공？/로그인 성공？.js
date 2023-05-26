function solution(id_pw, db) {
    let result
    db.map(item => {
        if(item[0] === id_pw[0] && item[1] === id_pw[1]) {
            result = 'login'
        } else if (item[0] === id_pw[0] && item[1] !== id_pw[1]) {
            result = 'wrong pw'
        } else if (item[0] !== id_pw[0] && item[1] !== id_pw[1]){
            result = 'fail'        
        }
    })
    return result
}