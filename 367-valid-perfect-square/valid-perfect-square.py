class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r = num
        while l<=r:
            middle = l+((r-l)//2)

            if middle**2 == num:
                return True
            elif middle**2 > num:
                r=middle-1
            else:
                l=middle+1

        return False