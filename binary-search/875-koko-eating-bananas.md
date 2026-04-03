### My answer

Binary search: Time O(mlog(n)) Space O(1)

```jx
var minEatingSpeed = function(piles, h) {
    let l = 1
    let r = Math.max(...piles)
    let res = Infinity

    const getHours = (a) => {
        return piles.reduce((prev, curr) => {
            return prev += Math.ceil(curr / a)
        }, 0)
    }

    while (l <= r) {
        const mid = Math.floor((r + l + 1) / 2)
        const hours = getHours(mid)
        if (hours > h) {
            l = mid + 1
        } else {
            r = mid - 1
            res = Math.min(res, mid)
        }
    }
    return res
};
```
