class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        for i in range(n):
            res += 4 * i
        return res

# recursion
class Solution:
    def coloredCells(self, n: int) -> int:
        # 0: 0^2 - 4*0
        # 1: 1^2 - 4*0
        # 2: 3^2 - 4*1
        # 3: 5^2 - 4*3
        # 4: 7^2 - 4*6
        # n: (2n - 1)^2 - 4*(b + n - 1)
        def count(i, curr, b):
            if i == n + 1:
                return curr
            if i > 1:
                b = b + i - 1
            curr = (2 * i - 1)**2 - 4 * b
            return count(i + 1, curr, b)

        return count(0, 0, 0)