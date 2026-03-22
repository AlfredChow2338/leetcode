### Takeaways

1. Each height's water = `min(leftMax[i], rightMax[i]) - height[i]`

2. Brute force: Time Complexity O(n^2) Memory Complexity O(1)

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

2. Prefix sum: Time Complexity O(n) Memory Complexity O(n)

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

3. Two pointers: Time Complexity O(n) Memory Complexity O(1)

```js
var trap = function(height) {
    const n = height.length
    let res = 0
        l = 0
        r = n - 1
        leftMax = height[l]
        rightMax = height[r]
        
    while (l <= r) {
        if (leftMax > rightMax) {
            res += Math.max(Math.min(leftMax, rightMax) - height[r], 0)
            rightMax = Math.max(rightMax, height[r])
            r --
        } else {
            res += Math.max(Math.min(leftMax, rightMax) - height[l], 0)
            leftMax = Math.max(leftMax, height[l])
            l ++
        }
    }

    return res
};
```


### My answers