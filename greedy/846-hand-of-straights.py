from typing import Counter, List

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
