### Takeaways

1. `Math.trunc` returns the integer part of a number by removing any fractional digits.

2. Be careful about the string and integer types when we store and operate. 

3. Recursion because every operator applies to the two most recent values that come before it.

```js
const dfs = () => {
    const token = tokens.pop();
    if (!'+-*/'.includes(token)) {
        return parseInt(token);
    }

    const right = dfs();
    const left = dfs();

    if (token === '+') {
        return left + right;
    } else if (token === '-') {
        return left - right;
    } else if (token === '*') {
        return left * right;
    } else {
        return Math.trunc(left / right);
    }
};

return dfs();
```

### My answers

```js
var evalRPN = function(tokens) {
    const numSt = []
    let op = null
    const ops = ['+', '-', '*', '/']

    const calculate = (aStr, bStr, operator) => {
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
            op = t
        } else {
            numSt.push(t)
        }

        if (op) {
            const n2 = numSt.pop()
            const n1 = numSt.pop()            
            if (n1 && n2) {
                numSt.push(calculate(n1, n2, op))
            }
            op = null
        }
    }
    return parseInt(numSt[0])
};
```