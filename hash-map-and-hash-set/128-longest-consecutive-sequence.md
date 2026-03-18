### Takeaways

1. Use hash set to make number unique and read O(1). Early return to reduce repeated lookup. 

```jsx
var longestConsecutive = function(nums) {
    const hashSet = new Set(nums)
    let max = 0
    for (let i = 0; i < nums.length; i++) {
        if (hashSet.has(nums[i] - 1)) {
            continue
        }
        let currentMax = 1
        while (hashSet.has(nums[i] + currentMax)) {
            currentMax += 1
        }
        max = Math.max(max, currentMax)
    }
    return max
};
```

2. Check upper boundary and lower boundary: when we place a new number into the map, it may connect two existing sequences or extend one of them. Instead of scanning forward or backward, we only look at the lengths stored at the neighbors:

```jsx
var longestConsecutive = function(nums) {
    const map = new Map()
    let max = 0
    for (const n of nums) {
        if (map.has(n)) {
            continue
        }
        map.set(n, (map.get(n-1) ?? 0) + (map.get(n+1) ?? 0) + 1)
        map.set(n - (map.get(n-1) ?? 0), map.get(n));
        map.set(n + (map.get(n+1) ?? 0), map.get(n));
        max = Math.max(max, map.get(n))
    }
    return max
};
```