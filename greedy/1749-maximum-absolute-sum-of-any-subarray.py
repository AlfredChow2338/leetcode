from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum, max_sum, prefix_sum = 0, 0, 0

        for n in nums:
          prefix_sum += n
          min_sum = min(min_sum, prefix_sum)
          max_sum = max(max_sum, prefix_sum)

        return max_sum - min_sum

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        arr_map = {n:i for i, n in enumerate(arr)}
        max_len = 0
        n = len(arr)
        dp = {} # (i, j) -> longest length

        for i in reversed(range(n - 1)):
            for j in reversed(range(i + 1, n)):
                prev, curr = arr[i], arr[j]
                nxt = prev + curr
                curr_len = 2

                if nxt in arr_map:
                    curr_len = 1 + dp[(j, arr_map[nxt])]
                    max_len = max(max_len, curr_len)
                dp[(i, j)] = curr_len

        return max_len  