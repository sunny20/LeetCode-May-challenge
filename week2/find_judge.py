class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N ==1:
            return 1
        dic = {}
        for a,b in trust:
            if a not in dic:
                dic[a] = -1
            else:
                dic[a] -= 1

            if b not in dic:
                dic[b] = 1
            else:
                dic[b] += 1
        for k,v in dic.items():
            if v == N-1:
                return k
        return -1