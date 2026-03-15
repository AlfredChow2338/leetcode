### Takeaways

1. by thinking `result[i] = pref[i] × suff[i]`, we know we need to construct 2 arrays: prefix sum and suffix sum.
```jsx
var productExceptSelf = function(nums) {
    const n = nums.length
    const prefix = Array(n).fill(0)
    const suffix = Array(n).fill(0)
    const res = Array(n).fill(0)
    prefix[0] = 1
    suffix[n-1] = 1
    for (let i = 1; i < n; i++) {
        prefix[i] = prefix[i-1] * nums[i-1]
    }
    for (let i = n - 2; i >= 0; i--) {
        suffix[i] = suffix[i+1] * nums[i+1]
    }
    for (let i = 0; i < n; i++) {
        res[i] = prefix[i] * suffix[i]
    }
    return res
}
```

2. division is the simple approach which requires to think about all conditions:

* If there are two or more zeros, then every product will include at least one zero → the entire res is all zeros.
* If there is exactly one zero, then only the position containing that zero will get the product of all non-zero numbers. All other positions become 0.
* If there are no zeros, we can safely do:
result[i] = total_product // nums[i]

```jsx
var productExceptSelf = function(nums) {
    const n = nums.length
        res = Array(n).fill(0)
    let zeros = 0
        product = 1
    for (let i = 0; i < nums.length; i++) {
        if (nums[i]) {
            product = product * nums[i]
        } else {
            zeros ++
        }
    }
    if (zeros > 1) {
        return Array(n).fill(0)
    }
    if (zeros === 1) {
        res[nums.indexOf(0)] = product
        return res
    }
    for (let i = 0; i < nums.length; i++) {
        if (nums[i]) {
            res[i] = product / nums[i]
        }
    }
    return res
}
```

### My answers
