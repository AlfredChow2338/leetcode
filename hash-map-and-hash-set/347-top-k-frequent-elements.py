from typing import List

# Bucket Sort
# Runtime: 119 ms, faster than 6.47% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 22.2 MB, less than 6.24% of Python3 online submissions for Top K Frequent Elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                print(res)
                if len(res) == k:
                    return res
                
# Sorted Hash Map
# Runtime: 80 ms, faster than 92.65% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 21.2 MB, less than 43.00% of Python3 online submissions for Top K Frequent Elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map n: count
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
            
        # sort map by count values
        sd = sorted(d.items(), key=lambda item: item[1], reverse=True)
        
        res: List[int] = []
        for i in range(k):
            res.append(sd[i][0])

        return res 