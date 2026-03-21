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

