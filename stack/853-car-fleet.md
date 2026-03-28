### Takeaways

1. Stack: Time O(nlog(n)) Space O(n)
```js
var carFleet = function(target, position, speed) {
    const len = position.length
    const roundToTargetMap = new Map() 
    const st = []
    for (let i = 0; i < len; i++) {
        roundToTargetMap.set(position[i], (target - position[i]) / speed[i]) 
    }
    position.sort((a, b) => a - b)
    for (let i = len - 1; i >= 0; i--) {
        st.push(roundToTargetMap.get(position[i]))
        if (st.length >= 2 && st[st.length - 1] <= st[st.length - 2]) {
            st.pop()
        }
    }
    return st.length
};
```

### My answer

Hashmap: Time O(nlog(n)) Space O(n)

```js
var carFleet = function(target, position, speed) {
    const len = position.length
    const roundToTargetMap = new Map()
    const positionSpeedMap = new Map()
    let res = len
    for (let i = 0; i < len; i++) {
        positionSpeedMap.set(position[i], speed[i])
        roundToTargetMap.set(position[i], (target - position[i]) / speed[i]) 
    }
    position.sort((a, b) => a - b)
    for (let i = len - 2; i >= 0; i--) {
        j = i + 1 // i = back, j = front
        if (roundToTargetMap.get(position[i]) <= roundToTargetMap.get(position[j])) {
            roundToTargetMap.set(position[i], roundToTargetMap.get(position[j]))
            res -= 1
        }
    }
    return res
};
```