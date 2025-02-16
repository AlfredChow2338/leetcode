# Runtime: 42 ms, faster than 80.22% of Python3 online submissions for Roman to Integer.
# Memory Usage: 16.6 MB, less than 46.46% of Python3 online submissions for Roman to Integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        
        i = 0
        res = 0

        while i < len(s):
            st = ""
            if i < len(s) - 1:
                st = s[i:i+2]
            else:
                st = s[i:i+1]

            if st == "IV" or st == "IX" or st == "XL" or st == "XC" or st == "CD" or st == "CM":
                i += 1
            else:
                st = s[i:i+1]
            
            res += m[st]
            i += 1

        return res