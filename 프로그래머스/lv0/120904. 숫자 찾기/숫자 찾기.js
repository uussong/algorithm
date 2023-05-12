const solution = (num, k) => {
    const index = num.toString().split('').findIndex(n => n == k)
    return index === -1 ? -1 : index + 1
}