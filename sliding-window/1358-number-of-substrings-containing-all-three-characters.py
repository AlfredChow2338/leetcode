from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n, left, res = len(s), 0, 0
        count = defaultdict(int)
        for right in range(n):
            count[s[right]] = 1 + count.get(s[right], 0)
            while len(count) == 3:
                res += n - right
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
        return res 