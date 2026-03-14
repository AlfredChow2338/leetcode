### Takeaways
1. to sort map by values, this requires map to sorted array
```jsx
const sorted = Array.from(map.entries()).sort((a, b) => b[1] - a[1])
```

2. min-heap is perfect for this because it always keeps the smallest element at the top.
```jsx
const heap = new MinPriorityQueue(x => x[1])
for (const item of Array.from(map.entries())) {
    heap.enqueue(item)
    if (heap.size() > k) {
        heap.dequeue()
    }
}
for (let i = 0; i < k; i++) {
    const [n] = heap.dequeue()
    res.push(n)
}
```

3. bucket sort can be used where we directly jump to the most frequent numbers without sorting all the elements by frequency.
```jsx
var topKFrequent = function(nums, k) {
    const map = new Map()
    const bucket = Array.from({ length: nums.length + 1 }, () => [])
    const res = []
    for (const n of nums) {
        map.set(n, map.has(n) ? map.get(n) + 1 : 1)
    }
    const keys = Array.from(map.keys())
    for (const n of keys) {
        bucket[map.get(n)].push(n)
    }
    for (let i = nums.length; i >= 0; i --) {
        for(const n of bucket[i]) {
            res.push(n)
        }
        if (res.length === k) {
            return res
        }
    }
    return res
};
```

### My answers

```jsx
var topKFrequent = function(nums, k) {
    const map = new Map()
    const res = []
    for (const n of nums) {
        map.set(n, map.has(n) ? map.get(n) + 1 : 1)
    }
    const sorted = Array.from(map.entries()).sort((a, b) => b[1] - a[1])
    console.log(sorted)
    for (let i = 0; i < k; i++) {
        res.push(sorted[i][0])
    }
    return res
};
```