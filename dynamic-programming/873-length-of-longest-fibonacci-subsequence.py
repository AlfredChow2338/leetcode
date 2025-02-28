from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # dp[prev][curr] stores length of Fibonacci sequence ending at indexes prev,curr
        dp = [[0] * n for _ in range(n)]
        max_len = 0

        # Find all possible pairs that sum to arr[curr]
        for curr in range(2, n):
            # Use two pointers to find pairs that sum to arr[curr]
            start = 0
            end = curr - 1

            while start < end:
                pair_sum = arr[start] + arr[end]

                if pair_sum > arr[curr]:
                    end -= 1
                elif pair_sum < arr[curr]:
                    start += 1
                else:
                    # Found a valid pair, update dp
                    dp[end][curr] = dp[start][end] + 1
                    max_len = max(dp[end][curr], max_len)
                    end -= 1
                    start += 1

        # Add 2 to include first two numbers, or return 0 if no sequence found
        return max_len + 2 if max_len else 0
    
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