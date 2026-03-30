### My answer

Binary Search: Time (logn) Space(1)

```js
var search = function(nums, target) {
    let l = 0
    let r = nums.length - 1
    while (l <= r) {
        const mid = Math.floor((l + r) / 2)
        if (nums[mid] === target) {
            return mid
        }
        if (nums[mid] > target) {
            r = mid - 1
        } else {
            l = mid + 1
        }
    }
    return -1
};
```