from typing import List

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
      pizzas.sort()
      days = len(pizzas) // 4
      odd_days = (days + 1) // 2
      even_days = days // 2
      low, high = 0, len(pizzas) - 1
      res = 0
      
      for _ in range(odd_days):
          res += pizzas[high]
          high -= 1
          low += 3
      
      for _ in range(even_days):
          res += pizzas[high - 1]
          high -= 2
          low += 2
      
      return res