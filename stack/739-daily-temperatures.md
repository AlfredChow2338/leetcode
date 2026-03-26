### Takeaways

### My answers

Brute Force: Time limit exceeded
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