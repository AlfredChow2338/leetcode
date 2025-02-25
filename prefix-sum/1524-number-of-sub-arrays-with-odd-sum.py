from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = prefix_sum = 0
        odd_count, even_count = 0, 1

        for n in arr:
          prefix_sum += n
          if prefix_sum % 2 == 0:
            count += odd_count
            even_count += 1
          else:
            count += even_count
            odd_count += 1
          count %= MOD

        return count