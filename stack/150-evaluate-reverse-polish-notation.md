### Takeaways

### My answers

```js
var evalRPN = function(tokens) {
    const numSt = []
    const opSt = []
    const ops = ['+', '-', '*', '/']

    const calculate = (aStr, bStr, operator) => {
        if (!aStr.length || !bStr.length || !operator.length) {
            return
        }
        let ans = 0
        const a = parseInt(aStr)
            b = parseInt(bStr)
        if (operator === '+') {
            ans = a + b
        }
        if (operator === '-') {
            ans =  a - b
        }
        if (operator === '*') {
            ans =  a * b
        }
        if (operator === '/') {
            ans =  Math.trunc(a / b)
        }
        return String(ans)
    }

    for (const t of tokens) {
        if (ops.includes(t)) {
            opSt.push(t)
        } else {
            numSt.push(t)
        }

        if (opSt.length > 0) {
            const n2 = numSt.pop()
            const n1 = numSt.pop()
            const operator = opSt.pop()
            if (n1 && n2 && operator) {
                numSt.push(calculate(n1, n2, operator))
            }
        }
    }
    return parseInt(numSt[0])
};
```