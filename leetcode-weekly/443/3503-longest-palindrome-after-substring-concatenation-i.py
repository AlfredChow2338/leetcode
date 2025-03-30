class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def isPali(s):
            return s == s[::-1]
        res, n, m = 0, len(s), len(t)
        for i in range(n + 1):
            for j in range(i, n + 1):
                ss = s[i:j]
                for k in range(m + 1):
                    for l in range(k, m + 1):
                        ts = t[k:l]
                        combined = ss + ts
                        if isPali(combined):
                            res = max(res, len(combined))
        return res