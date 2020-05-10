class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while l<= r:
            mid = int((l+r)/2)
            print(l,mid,r)
            if mid*mid == num:
                return True
            elif mid*mid < num:
                l=mid+1
            elif mid*mid > num:
                r=mid-1
                
        return False