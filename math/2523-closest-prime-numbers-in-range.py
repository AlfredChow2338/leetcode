from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        min_diff = float("inf")
        res = [-1, -1]
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(right**0.5) + 1):
            for j in range(i * i, right + 1, i):
                is_prime[j] = False

        prime_nums = [num for num in range(left, right + 1) if is_prime[num]]
        
        if len(prime_nums) < 2:
            return res
        
        for i in range(len(prime_nums) - 1):
            diff = prime_nums[i+1] - prime_nums[i]
            if diff < min_diff:
                res[0], res[1] = prime_nums[i], prime_nums[i+1]
            min_diff = min(min_diff, diff)
        
        return res
