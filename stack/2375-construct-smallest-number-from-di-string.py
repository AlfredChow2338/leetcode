class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, st = [], []
        for i in range(len(pattern) + 1):
            st.append(i+1)
            while st and (i == len(pattern) or pattern[i] == "I"):
                res.append(str(st.pop()))
        return "".join(res)
