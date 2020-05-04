class Solution:
    def findComplement(self, num: int) -> int:
        max_base = 2
        while max_base <=num:
            max_base *=2
        return max_base-1-num