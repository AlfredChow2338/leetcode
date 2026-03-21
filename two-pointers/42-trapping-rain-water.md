### Takeaways

1. Brute force

```js
var trap = function(height) {
    let res = 0
    for (let i = 0; i < height.length; i++) {
        let leftMax = height[i]
            rightMax = height[i]
        for (let j = 0; j < i; j ++) {
            leftMax = Math.max(leftMax, height[j])
        }
        for (let j = i + 1; j < height.length; j++) {
            rightMax = Math.max(rightMax, height[j])
        }
        res += Math.min(leftMax, rightMax) - height[i]
    }
    return res
};
```

2. Prefix sum

```js
var trap = function(height) {
    let res = 0
        leftMax = 0
        rightMax = 0
    const n = height.length
        prefix = Array(n).fill(0)
        suffix = Array(n).fill(0)
        
    for (let i = n - 1; i >= 0; i--) {
        rightMax = Math.max(rightMax, height[i])
        suffix[i] = rightMax
    }
    for (let i = 0; i < n; i++) {
        leftMax = Math.max(leftMax, height[i])
        prefix[i] = leftMax
        res += Math.min(prefix[i], suffix[i]) - height[i]
    }
    return res
};
```


### My answers