class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic = {}
        for s in S:
            if s in J:
                if s in dic:
                    dic[s] +=1
                else:
                    dic[s]  = 1
        return sum(dic.values())
        