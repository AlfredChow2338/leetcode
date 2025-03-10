# Time limit exceeded
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        m = { "a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "other": 0 }
        res, left, l = 0, 0, 0

        def getKey(c: str) -> str:
            if c != "a" and c != "e" and c != "i" and c != "o" and c != "u":
                return "other"
            return c

        for right in range(len(word)):
            m[getKey(word[right])] += 1
            
            left = right - sum(list(m.values())) + 1

            tempLeft = left
            
            while m["a"] > 0 and m["e"] > 0 and m["i"] > 0 and m["o"] > 0 and m["u"] > 0 and m["other"] >= k:
                if m["other"] == k:
                    res += 1
                m[getKey(word[left])] -= 1
                left += 1
            
            for i in range(tempLeft, left):
                m[getKey(word[i])] += 1

            left = tempLeft
            
        return res

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        res = 0

        def isVowel(c: str) -> bool:
            return c in ["a", "e", "i", "o", "u"]
            
        for i in range(k, k+2):
            m = {}
            left, right, consonantCount = 0, 0, 0
            while right < len(word):
                ch = word[right]
                if isVowel(ch):
                    m[ch] = m.get(ch, 0) + 1
                else:
                    consonantCount += 1
                while len(m) == 5 and consonantCount >= i:
                    if i == k:
                        res += len(word) - right
                    else:
                        res -= len(word) - right
                    leftCh = word[left]
                    if isVowel(leftCh):
                        m[leftCh] -= 1
                        if m[leftCh] == 0:
                            del m[leftCh]
                    else:
                        consonantCount -= 1
                    left += 1
                right += 1
        return res

