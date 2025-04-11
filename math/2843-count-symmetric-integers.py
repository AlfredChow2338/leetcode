class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        def isSym(n):
            l = len(str(n))
            if l % 2:
                return False
            mid = l // 2
            pre, suf = str(n)[mid:], str(n)[:mid]
            if pre == suf:
                return True
            left_sum, right_sum = 0, 0
            for i in range(mid):
                left_sum += int(pre[i])
                right_sum += int(suf[i])
            return left_sum == right_sum
        for n in range(low, high + 1):
            if isSym(n):
                res += 1
        return res
