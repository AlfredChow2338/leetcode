from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def check_unique(start):
            seen = set()
            for num in nums[start:]:
                if num in seen:
                    return False
                seen.add(num)
            return True

        ans = 0
        for i in range(0, len(nums), 3):
            if check_unique(i):
                return ans
            ans += 1
        return ans

# backward
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 1 <= nums[i] <= 100
        n = len(nums)
        seen = [False] * 101
        for i in range(n - 1, -1, -1):
            if seen[nums[i]]:
                return i // 3 + 1
            seen[nums[i]] = True
        return 0