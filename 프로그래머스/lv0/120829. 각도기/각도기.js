const solution = angle => {
    if (angle === 90) return 2
    if (angle === 180) return 4
    if (angle < 90) {
        return 1
    } else {
        return 3
    }
}