from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # 1:  000001
        # 3:  000011
        # 8:  001000
        # 10: 001010
        # 48: 110000
        # &: AND |: OR ^: XOR
        res, l, cb = 0, 0, 0
        for r in range(len(nums)):
            while cb & nums[r]:
                # cb: 001 ^ nums[l]: 001 = new cb: 000 
                # cb: 111011 ^ nums[l]: 000011 = new cb: 111000
                cb = cb ^ nums[l]
                l += 1
            res = max(res, r - l + 1)
            # cb: 000 | nums[r]: 001 = new cb: 001
            # cb: 000 | nums[r]: 011 = new cb: 011
            # cb: 0011 | nums[r]: 1000 = new cb: 1011
            cb = cb | nums[r]
        return res
            