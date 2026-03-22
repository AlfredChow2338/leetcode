### Takeaways

### My answers
```js
var isValid = function(s) {
    const st = []
    const mp = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    let res = true
    for (let i = 0; i < s.length; i++) {
        if (Object.keys(mp).includes(s[i])) {
            st.push(s[i])
            continue
        }
        if (Object.values(mp).includes(s[i])) {
            const top = st.pop()
            if (mp[top] !== s[i]) {
                res = false
                break
            }
        }
    }
    return res && st.length === 0
};
```