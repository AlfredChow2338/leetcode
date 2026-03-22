### Takeaways

1. Two stacks

```js

var MinStack = function() {
    this.st = []
    this.minSt = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.st.push(val)
    const newVal = Math.min(val, this.minSt.length > 0 ? this.minSt[this.minSt.length - 1] : val)
    this.minSt.push(newVal)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.st.pop()
    this.minSt.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.st[this.st.length - 1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.minSt[this.minSt.length - 1]
};
```

3. (Advanced) One stack with encoded value

```js

var MinStack = function() {
    this.st = []
    this.min = Infinity
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    console.log(this)
    if (!this.st.length) {
        this.min = val
        this.st.push(0)
        return
    }
    this.st.push(val - this.min)
    this.min = Math.min(this.min, val)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    console.log('pop', this)
    const pop = this.st.pop()
    if (pop < 0) {
        this.min -= pop
    }
    return this.min
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    console.log(this)
    let top = this.st[this.st.length - 1]
    if (top > 0) {
        return top + this.min
    }
    return this.min
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.min
};
```


### My answer

Brute force: getMin Time Complexity O(nlogn)

```js

var MinStack = function() {
    this.st = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.st.push(val)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.st.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    console.log(this.st)
    return this.st[this.st.length - 1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    const sorted = this.st.toSorted((a, b) => a - b)
    return sorted[0]
};
```