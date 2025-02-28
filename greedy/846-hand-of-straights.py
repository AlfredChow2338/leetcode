import heapq
from typing import Counter, List

# hashmap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
      if len(hand) % groupSize:
        return False
      hand.sort()
      count = Counter(hand)
      for n in hand:
        if count[n]:
          for i in range(n, n + groupSize):
            if not count[i]:
              return False
            count[i] -= 1
      return True

# min heap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
      if len(hand) % groupSize:
        return False

      count = {}
      
      for n in hand:
        count[n] = 1 + count.get(n, 0)
      
      minH = list(count.keys())
      heapq.heapify(minH)

      while minH:
        first = minH[0]

        for i in range(first, first + groupSize):
          if i not in count:
            return False
          count[i] -= 1
          if count[i] == 0:
            if i != minH[0]:
              return False
            heapq.heappop(minH)

      return True