### My answer

Hashmap: Time O(n) Space O(n)

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