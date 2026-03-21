### Takeways

1. The algorithm requires moving the pointer at the shorter height inward. Moving the taller pointer instead never increases the area (since height is limited by the shorter side) and can cause the algorithm to miss the optimal solution.

### My answers

Brute force

```js
var maxArea = function(height) {
    let res = 0
    for (let i = 0; i < height.length; i++) {
        for (let j = 0; j < height.length; j++) {
            const area = Math.min(height[i], height[j]) * Math.abs(i - j)
            res = Math.max(res, area)
        }
    }
    return res
};
```

Two Pointers
```js
var maxArea = function(height) {
    let res = 0
        l = 0
        r = height.length - 1
    while (l <= r) {
        const area = Math.min(height[l], height[r]) * (r - l)
        res = Math.max(res, area)
        if (height[l] > height[r]) {
            r --
        } else {
            l ++
        }
    }
    return res
};
```