class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True

        if len(s) <= 1:
            return False

        globalL = {}
        globalR = {}

        for i, ch in enumerate(s):
            if ch not in globalL:
                globalL[ch] = i
            globalR[ch] = i

        candidates = []
        
        for i in range(len(s)):
            if i != globalL[s[i]]:
                continue
            j = globalR[s[i]]
            x = i
            while x <= j:
                j = max(j, globalR[s[x]])
                x += 1
            
            valid = True
            for x in range(i, j + 1):
                if globalL[s[x]] < i or globalR[s[x]] > j:
                    valid = False
                    break

            if valid and not (i == 0 and j == len(s) - 1):
                candidates.append((i, j))
        
        candidates.sort(key=lambda interval: interval[1])
        
        count = 0
        end = -1

        for (start, finish) in candidates:
            if start > end:
                count += 1
                end = finish

        return count >= k