### Takeaways

1. hash table can be applied to replace string sort
```jsx
const ht = Array(26).fill(0)
for (let i = 0; i < str.length; i++) {
    ht[str.charCodeAt(i) - "a".charCodeAt(0)] += 1
}
const key = ht.join(",")
```

2. when converting frequency counts to strings, using a naive format like concatenation without separators can cause collisions. 
For example, counts [1,11] and [11,1] could produce the same string "111".

### My answers

```jsx
var groupAnagrams = function(strs) {
    const map = new Map()
    for (const str of strs) {
        const key = str.split("").sort().join("")
        if (map.has(key)) {
            map.set(key, [...map.get(key), str])
        } else {
            map.set(key, [str])
        }
    }
    return Array.from(map.values())
};
```