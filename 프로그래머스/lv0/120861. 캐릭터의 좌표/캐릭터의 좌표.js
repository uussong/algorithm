function solution(keyinput, board) {
    const leftRight = Math.floor(board[0] / 2)
    const upDown = Math.floor(board[1] / 2)

    const result = [0, 0]
    for(const key of keyinput) {
        switch (key) {
            case 'left':
                result[0] -= 1
                if (result[0] < -leftRight) {
                    result[0] = -leftRight
                }
                break
            case 'right':
                result[0] += 1
                if (result[0] > leftRight) {
                    result[0] = leftRight
                }
                break
            case 'down':
                result[1] -= 1
                if (result[1] < -upDown) {
                    result[1] = -upDown
                }
                break
            case 'up':
                result[1] += 1
                if (result[1] > upDown) {
                    result[1] = upDown
                }
                break
        }
    }

    return result
}