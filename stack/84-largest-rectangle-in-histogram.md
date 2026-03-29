### Takeaways

1. Brute force: Time O(n^2). To find how wide this rectangle can extend, we look left and right until we hit a bar shorter than the current one.
```js
var largestRectangleArea = function(heights) {
    const n = heights.length;
    let maxArea = 0;

    for (let i = 0; i < n; i++) {
        const h = heights[i]
        let l = i
        let r = i + 1
        while (l >= 0 && heights[l] >= h) {
            l--
        }
        while (r < n && heights[r] >= h) {
            r ++
        }
        l ++
        const w = r - l
        maxArea = Math.max(maxArea, w * h)
    }
    return maxArea;
};
```

2. Stack

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