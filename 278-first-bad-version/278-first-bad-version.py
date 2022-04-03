# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        j = n 
        while(i<j):
            pivot = (i+j)//2
            if(isBadVersion(pivot)):
                j = pivot
            else:
                i = pivot + 1
        return i
