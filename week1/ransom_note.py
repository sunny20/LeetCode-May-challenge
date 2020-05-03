class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for ch in ransomNote:
            if ch not in dic:
                dic[ch] = 1 
            else:
                dic[ch] += 1
        for ch in magazine:
            if ch in dic:
                if dic[ch] > 0:
                    dic[ch] -= 1
        for v in dic.values():
            if v > 0:
                return False
        return True