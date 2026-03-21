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


### My answers