# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        start_version = 1
        end_version = n
        while start_version<=end_version:
            middle = int((end_version-start_version)/2 + start_version )

            print(start_version,end_version,middle)
            if isBadVersion(middle) == False:
                if isBadVersion(middle+1) == True:
                    return middle+1
                start_version = middle+1
            elif isBadVersion(middle) == True:
                if isBadVersion(middle-1) == False:
                    return middle
                end_version = middle-1
        return None
