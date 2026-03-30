### My answers

Binary Search I: Time O(n) Space O(1)

```js
var searchMatrix = function(matrix, target) {
    let row = -1
    let res = false
    for (let i = 0; i < matrix.length; i++) {
        if (target === matrix[i][0]) {
            return true
        }
        if (target > matrix[i][0]) {
            row += 1
        } else {
            break
        }
    }
    let l = 0
    row = Math.max(row, 0)
    let r = matrix[row].length
    while (l <= r) {
        const mid = Math.floor((l + r) / 2)
        if (matrix[row][mid] === target) {
            return true
        }
        if (matrix[row][mid] > target) {
            r = mid - 1
        } else {
            l = mid + 1
        }
    }
    return false
};
```

Binary Search II: Time(logn) Space O(1)

```js
var searchMatrix = function(matrix, target) {
    const ROWS = matrix[0].length
    const COLS = matrix.length
    let res = false
    let top = 0
    let bot = COLS - 1
    let l = 0
    let r = ROWS - 1
    
    while (top <= bot) {
        const mid = Math.floor((top + bot) / 2)
        if (target === matrix[mid][0]) {
            res = true
            break
        }
        if (matrix[mid][0] > target) {
            bot = mid - 1
        } else {
            top = mid + 1
        }
    }

    const row = Math.max(Math.floor((top + bot) / 2), 0)

    while (l <= r) {
        const mid = Math.floor((l + r) / 2)
        if (matrix[row][mid] === target) {
            return true
        }
        if (matrix[row][mid] > target) {
            r = mid - 1
        } else {
            l = mid + 1
        }
    }
    return false
};
```