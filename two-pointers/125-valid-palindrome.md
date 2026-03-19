### Takeaways

1. Check alphanumeric can be simple as:
```jsx
return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' || c >= '0' && c <= '9'
```

2. While loop approach inside make sure inside while loop also check (l < r)
```jsx
while (l <= r) {
    while (l < r && !isAlphanum(s[l])) {
        l ++
    }
    while (l < r && !isAlphanum(s[r])) {
        r --
    }
    if (s[l].toLowerCase() !== s[r].toLowerCase()) {
        return false
    }
    l ++
    r --
}
```

3. Reverse string approach
```jsx
let newStr = '';
for (let c of s) {
    if (this.isAlphanumeric(c)) {
        newStr += c.toLowerCase();
    }
}
return newStr === newStr.split('').reverse().join('');
```

### My answers
```jsx
var isPalindrome = function(s) {
    let l = 0
        r = s.length - 1
    const isChar = (c) => {
        return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' || c >= '0' && c <= '9'
    }
    while (l <= r) {
        const lc = s.substr(l, 1).toLowerCase()
              rc = s.substr(r, 1).toLowerCase()
        if (!isChar(lc)) {
            l ++
            continue
        }
        if (!isChar(rc)) {
            r --
            continue
        }
        if (lc !== rc) {
            return false
        }
        l ++
        r --
    }
    return true
};
```