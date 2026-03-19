### Takeaways

1. Binary Search: because the array is already sorted, we don’t need to check every pair. 

```js
var twoSum = function(numbers, target) {
    const len = numbers.length
    for (let i = 0; i < len; i++) {
        let l = i + 1
            r = len - 1
        const diff = target - numbers[i]
        while (l <= r) {
            const mid = l + Math.floor((r - l) / 2)
            const midVal = numbers[mid]
            if (midVal === diff) {
                return [i + 1, mid + 1]
            }
            if (midVal > diff) {
                r = mid - 1
            } else {
                l = mid + 1
            }
        }
    }
    return []
};
```

2. Hash Map stores `{ number: index }` and find if diff exists in map

```jsx
var twoSum = function(numbers, target) {
    const len = numbers.length
    const map = new Map()
    for (let i = 0; i < numbers.length; i++) {
        const diff = target - numbers[i]
        if (map.has(diff)) {
            return [map.get(diff)+1, i+1]
        }
        map.set(numbers[i], i)
    }
    return
};
```

### My answers

```jsx
var twoSum = function(numbers, target) {
    let l = 0
        r = numbers.length - 1
    while (l < r) {
        const diff = target - numbers[l] - numbers[r]
        if (diff === 0) {
            return [l + 1, r + 1]
        }
        if (diff < 0) {
            r --
        } else {
            l ++
        }
    }
};
```