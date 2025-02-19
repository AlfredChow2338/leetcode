class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * 2 ** (n - 1)
        res = []
        choices = "abc"
        left, right = 1, total

        for _ in range(n):
            cur = left
            partition_size = (right - left + 1) // len(choices)
            for c in choices:
                if k in range(cur, cur + partition_size):
                    res.append(c)
                    choices = "abc".replace(c, "")
                    left = cur
                    right = cur + partition_size
                    break
                cur += partition_size

        return "".join(res)

# backtracking
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr_str = ""
        happy_strs = []

        def generate_happy_strs(curr_str, happy_strs):
            if len(curr_str) == n:
                happy_strs.append(curr_str)
                return
            for c in "abc":
                if len(curr_str) > 0 and curr_str[-1] == c:
                    continue
                generate_happy_strs(curr_str + c, happy_strs)

        generate_happy_strs(curr_str, happy_strs)
        
        if len(happy_strs) < k:
            return ""
        
        happy_strs.sort()
        return happy_strs[k - 1]