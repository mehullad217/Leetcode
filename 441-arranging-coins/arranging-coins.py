class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=0
        r= n
        highest  = 0
        while l<=r:
            middle = l+((r-l)//2)
            if middle*(middle+1)/2<=n:
                l=middle+1
                highest = max(highest,middle)

            elif middle*(middle+1)/2>n:
                r=middle-1

        return highest
        