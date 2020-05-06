class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i,ch in enumerate(s):
            if ch not in dic:
                dic[ch] = i
            else:
                dic[ch] = -1
        for k,v in dic.items():
            if v !=-1:
                return v
        return -1
                
       