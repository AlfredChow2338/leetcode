### Takeaways

1. A simple and reliable strategy is to ***record the length of each string*** first, followed by a special separator, and then append all the strings together.

2. `String.prototype.substr()` vs `String.prototype.substring()`
```jsx
const word = "alfredislazy"
// to retrieve "lazy"
word.substr(8, 4)
word.substring(8, 12)
```

### My answers

```jsx
class Solution {
    encode(strs) {
        if (strs.length === 0) {
            return ''
        }
        const sizes = strs.map((s) => s.length)
        let res = sizes.join(',')
        res += ',#'
        for (const str of strs) {
            res += str
        }
        return res
    }

    decode(str) {
        const split = str?.split(',#')
        if (split.length !== 2) {
            return []
        }
        const sizes = split[0].split(',')
        const s = split[1]
        const res = [] 
        let idx = 0
        for (const size of sizes) {
            const word = s.substring(idx, idx + parseInt(size))
            res.push(word)
            idx += parseInt(size)
        }
        return res
    }
}
```