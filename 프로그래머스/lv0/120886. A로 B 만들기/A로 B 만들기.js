function solution(before, after) {
    let result 
    if(before.split("").sort().join("") === after.split("").sort().join("")) {
        result = 1
    } else {
        result = 0
    }
    return result
}