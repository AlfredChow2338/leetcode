from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(1 for num in set(nums) if num > k) if min(nums) >= k else -1