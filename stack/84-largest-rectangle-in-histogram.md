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

2. Stack: Time O(n) Space O(n). To efficiently find the nearest smaller bar on both sides, we use a monotonic stack that keeps indices of bars in increasing height order.

```js
var largestRectangleArea = function(heights) {
    const n = heights.length;
    let maxArea = 0;
    let st = []
    const leftMost = Array(n).fill(-1)
    const rightMost = Array(n).fill(n)

    for (let i = 0; i < n; i++) {
        while (st.length && heights[st[st.length - 1]] >= heights[i]) {
            st.pop()
        }
        if (st.length) {
            leftMost[i] = st[st.length - 1]
        }
        st.push(i)
    }
    st.length = 0
    for (let i = n - 1; i >= 0; i--) {
        while (st.length && heights[st[st.length - 1]] >= heights[i]) {
            st.pop()
        }
        if (st.length) {
            rightMost[i] = st[st.length - 1]
        }
        st.push(i)
    }

    for (let i = 0; i < n; i++) {
        leftMost[i] += 1;
        rightMost[i] -= 1;
        maxArea = Math.max(
            maxArea,
            heights[i] * (rightMost[i] - leftMost[i] + 1),
        );
    }

    return maxArea;
};
```


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