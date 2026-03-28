### My answer

Brute force: Time O(n^2)
```js
var largestRectangleArea = function(heights) {
    const len = heights.length
    const getArea = (i, j) => {
        const width = j - i
        const height = Math.min(...heights.slice(i, j))
        return width * height
    }
    let res = 0
    for (let i = 0; i < len; i++) {
        for (j = 0; j < len; j++) {
            if (i > j) continue
            const area = getArea(i, j + 1)
            res = Math.max(res, area)

        }
    }
    return res
};
```