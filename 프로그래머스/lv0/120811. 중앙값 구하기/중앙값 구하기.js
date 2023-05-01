const solution = array => {
    const middle = Math.floor(array.length / 2);
    array.sort((a, b) => a - b);

    return array[middle]
}