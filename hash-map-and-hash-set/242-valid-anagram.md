### Takeaway

1. sort string in js required `s.split('').sort().join('')`

2. `Map()` has many built-in functions similar to Object prototype eg. `keys()`, `values()`

3. hash table can be applied (best performance, beat 95% solutions)
```jsx
const count = new Array(26).fill(0);
for (let i = 0; i < s.length; i++) {
    count[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
    count[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
}
```


### My answers

1. Sorting

```jsx
var isAnagram = function(s, t) {
    if (s.length != t.length) {
        return false
    }
    const sortedS = s.split('').sort().join('')
    const sortedT = t.split('').sort().join('')
    return sortedS === sortedT
};
```

2. Hashmap
```jsx
var isAnagram = function(s, t) {
    if (s.length != t.length) {
        return false
    }
    const map = new Map()
    for (let i = 0; i < s.length; i++) {
        const charS = s.substring(i, i+1)
        const charT = t.substring(i, i+1)
        map.set(charS, map.get(charS) ? map.get(charS) + 1 : 1)
        map.set(charT, map.get(charT) ? map.get(charT) - 1 : -1)
    }
    return Array.from(map.values()).every(n => n === 0)
};
```