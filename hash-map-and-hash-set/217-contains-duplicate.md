### Takeaway

1. return inside forEach is to exit the loop instead of causing whole function to early return the value

2. hash set is a better use case for unique value over map while value is not necessary

3. `Set()` has many built-in functions eg. `has()`, `add()`


### My answers

```jsx
var containsDuplicate = function(nums) {
  const map = new Map()
  let res = false
  nums.forEach(n => {
      if (map.get(n)) {
          res = true
          return
      }
      map.set(n, 1)
  })
  console.log({map})
  return res
};
```