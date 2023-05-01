const solution = array => {
    array.sort((a,b)=> a-b)
    let mode = -1;
    let current = array[0];
    let maxCount = 0;
    let count = 0;
    if(array.length === 1) return array[0]
    for(let i = 0; i < array.length; i++){
        count++
        if(array[i] !== array[i+1]){
            if(maxCount === count) {
                mode = -1
            } else if(maxCount < count) {
                maxCount = count
                mode = array[i]
            }
            count = 0
        }
    }
    return mode
}