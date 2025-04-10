class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        start = str(start - 1)
        finish = str(finish)
        def calculate(st):
            if len(st) < len(s):
                return 0
            if len(st) == len(s):
                return 1 if st >= s else 0
            prefix_length = len(st) - len(s)
            suffix = st[prefix_length:]
            count = 0
            for i in range(prefix_length):
                if limit < int(st[i]):
                    count += (limit + 1) ** (prefix_length - i)
                    return count
                count += int(st[i]) * (limit + 1) ** (prefix_length - 1 - i)
            if suffix >= s:
                count += 1
            return count
        return calculate(finish) - calculate(start)