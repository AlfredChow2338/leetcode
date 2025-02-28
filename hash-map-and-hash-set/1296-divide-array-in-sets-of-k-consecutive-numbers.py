from typing import Counter, List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        nums.sort()
        count = Counter(nums)
        for n in nums:
            if count[n]:
                for i in range(n, n + k):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True
        
