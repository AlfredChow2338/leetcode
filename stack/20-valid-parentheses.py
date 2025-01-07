# Stack + Hashmap
# Runtime: 32 ms, faster than 77.21% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 16.5 MB, less than 89.12% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = { ')': '(', '}': '{', ']': '[' } 
        
        for c in s:
            if c in m:
                if stack and stack[-1] == m[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
                
        
                