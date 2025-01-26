from typing import List

class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
      res = []
      arr = [{ 'c': 0, 'on': True, 'offAt': 0 } for k in range(numberOfUsers)]
      sortedEvents = sorted(events, key=lambda x: (int(x[1]), reversor(ord(x[0][0])) ))
      print(sortedEvents)
      for event in sortedEvents:
        if event[0] == "OFFLINE":
          id = int(event[2])
          arr[id]['on'] = False
          arr[id]['offAt'] = int(event[1])
        elif event[0] == "MESSAGE":
          curTime = int(event[1])
          if event[2] == 'ALL':
            for user in arr:
              user['c'] += 1
          elif event[2] == 'HERE':
            for user in arr:
              if user['on']:
                user['c'] += 1
              elif not user['on'] and (curTime - user['offAt']) >= 60:
                user['c'] += 1
          else: 
            mentions = event[2:][0].split()
            for mention in mentions:
              id = int(mention[2:])
              user = arr[id]
              user['c'] += 1
      for user in arr:
        res.append(user['c'])
      return res
          
          