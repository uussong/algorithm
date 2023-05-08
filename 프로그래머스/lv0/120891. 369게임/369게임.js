function solution(order) {
    return String(order).replace(/[^369]/g, '').length
}