### Takeaways

1. Stack: Time O(n) Space O(n)

```js
var dailyTemperatures = function(temperatures) {
    const len = temperatures.length
        res = Array(len).fill(0)
        st = [] // [temp, index][]
    for (let i = 0; i < len; i++) {
        const currTemp = temperatures[i]
        while (st.length > 0 && currTemp > st[st.length-1][0]) {
            const [temp, idx] = st.pop()
            res[idx] = i - idx
        }
        st.push([currTemp, i])
    }
    return res
};
```

2. Dynamic programming: Time O(n) Space O(1). Instead of checking every future day one by one, we can reuse previously computed answers.

```js
var dailyTemperatures = function(temperatures) {
    const len = temperatures.length
        res = Array(len).fill(0)

    for (let i = len - 2; i >= 0; i--) {
        let j = i + 1
        while (j < len && temperatures[i] >= temperatures[j]) {
            if (res[j] === 0) {
                j = len
                break
            }
            j += res[j]
        }
        if (j < len) {
            res[i] = j - i
        }
    }
    return res
};
```

### My answers

Brute Force: Time Complexity O(n^2) Space Complexity O(1)
Time limit exceeded 

```js
var dailyTemperatures = function(temperatures) {
    const len = temperatures.length
        res = Array(len).fill(0)
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j ++) {
            if (i >= j) {
                continue
            }
            if (temperatures[j] > temperatures[i]) {
                res[i] = j - i
                break
            }
        }
    }
    return res
};
```