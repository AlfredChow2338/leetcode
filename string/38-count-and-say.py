class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        current = "1"
        for _ in range(2, n + 1):
            next_str = ""
            i = 0
            while i < len(current):
                count = 1
                while i + 1 < len(current) and current[i] == current[i + 1]:
                    i += 1
                    count += 1
                next_str += str(count) + current[i]
                i += 1
            current = next_str
        return current