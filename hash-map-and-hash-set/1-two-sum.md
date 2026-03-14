### Takeaway
1. `for of` doesn't work here because it loses track of index, using `indexOf` which only returns the first value index, causes issue for same values in `nums`

2. checking current index is not equal to previous complement index is necessary because same index is not allowed

3. sorting + two pointers can be applied
```jsx
var twoSum = function(nums, target) {
    const l = []
    for (let i = 0; i < nums.length; i++) {
        l.push([nums[i], i ])
    }
    l.sort((a, b) => a[0] - b[0])
    let i = 0
        j = nums.length - 1
    while (i < j) {
        const curr = l[i][0] + l[j][0]
        if (curr === target) {
            return [l[i][1], l[j][1]]
        }
        if (curr > target) {
            j -= 1
        } else {
            i += 1
        }
    }
    return []
};
```

4. best practice is single pass
```jsx
var twoSum = function(nums, target) {
    const map = new Map()
    for (let i = 0; i < nums.length; i++) {
        const comp = target - nums[i]
        if (map.has(comp) && map.get(comp) !== i) {
            return [map.get(comp), i]
        }
        map.set(nums[i], i)
    }
    return []
};
```

### My answers

```jsx
var twoSum = function(nums, target) {
    const map = new Map()
    for (let i = 0; i < nums.length; i++) {
        map.set(nums[i], i)
    }
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]
        if (map.has(complement) && map.get(complement) !== i) {
            return [map.get(complement), i]
        }
    }
    return []
};
```