from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        cook_m = {s: True for s in supplies} # [recipes that can cook]: 1
        recip_m = {r: i for i, r in enumerate(recipes)} # [recip]: recip index
        def dfs(recip):
            if recip in cook_m:
                return cook_m[recip]
            if recip not in recip_m:
                return False
            cook_m[recip] = False
            recip_i = recip_m[recip]
            for nei in ingredients[recip_i]:
                if not dfs(nei):
                    return False
            cook_m[recip] = True
            return cook_m[recip]
        for recip in recipes:
            if dfs(recip):
                res.append(recip)
        return res

