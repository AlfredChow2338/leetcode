### Takeaways

1. loop through 3 * 3 block
```jsx
for (let square = 0; square < 9; square++) {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            // use Math.floor(n / 3) * 3 + i
            const row = Math.floor(square / 3) * 3 + i
            // use (n % 3) * 3 + j
            const col = (square % 3) * 3 + j
        }
    }
}
```

2. use `Set`'s ' `add()` and `has()` methods are cleaner than using `Map` inside loops
```jsx
if (board[row][col] !== '.') {
    if (seen.has(board[row][col])) {
        return false;
    }
    seen.add(board[row][col]);
}
```

### Solution
```jsx
var isValidSudoku = function(board) {
    const len = board[0].length
    const rowSet = new Set()
    const colSet = new Set()
    let res = true

    for (let i = 0; i < len; i++) {
        const row = board[i]
        for (let j = 0; j < row.length; j++) {
            const rowCell = board[i][j]
            const colCell = board[j][i]
            if (rowCell !== '.') {
                if (rowSet.has(rowCell)) {
                    return false
                }
                rowSet.add(rowCell)
            }
            if (colCell !== '.') {
                if (colSet.has(colCell)) {
                    return false
                }
                colSet.add(colCell)
            }
        }
        rowSet.clear()
        colSet.clear()
    }

    for (let square = 0; square < 9; square++) {
        const sqSet = new Set()
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                const row = Math.floor(square / 3) * 3 + i
                const col = (square % 3) * 3 + j
                if (board[row][col] !== '.') {
                    if (sqSet.has(board[row][col])) {
                        return false;
                    }
                    sqSet.add(board[row][col]);
                }
            }
        }
    }
    return res
};
```