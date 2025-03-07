from typing import List

class TrieNode:
  def __init__(self):
    self.children = {}
    self.isWord = False

  def addWord(self, s: str):
    curr = self
    for c in s:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]
    curr.isWord = True
        
class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visited = set(), set()
        ROW, COL = len(board), len(board[0])
        root = TrieNode()

        for word in words:
          root.addWord(word)
        
        def dfs(r, c, node, word):
          coord = (r, c)
          if (r < 0 or
            r == ROW or
            c < 0 or
            c == COL or
            coord in visited or
            board[r][c] not in node.children):
            return
          
          curr_char = board[r][c]
          
          word += board[r][c]
          node = node.children[curr_char]
          if node.isWord:
            res.add(word)

          visited.add(coord)
          dfs(r + 1, c, node, word)
          dfs(r - 1, c, node, word)
          dfs(r, c + 1, node, word)
          dfs(r, c - 1, node, word)
          visited.remove(coord)
        
        for r in range(ROW):
          for c in range(COL):
            dfs(r, c, root, "")
        
        return list(res)


