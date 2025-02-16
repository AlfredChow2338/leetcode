# Array <-> String <-> Array
class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while(str[j] != '#'):
                j += 1
            length = int(str[i:j])
            s = str[j+1:j+1+length]
            res.append(s)
            i = j+1+length
            j = j+1+length
        return res