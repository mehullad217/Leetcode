# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=0
        r=n
        while l<=r:
            middle = l+ ((r-l)//2)

            if isBadVersion(middle):
                r=middle-1
            else:
                l=middle+1

        return l
                