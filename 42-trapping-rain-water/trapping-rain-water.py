class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=0
        rightmax=0
        l=0
        n=len(height)
        r=n-1
        total_water = 0
        for i in range(n):
            if leftmax<=rightmax:
                leftmax = max(leftmax, height[l])
                water_trapped = max(0, leftmax- height[l])
                l+=1

            else:
                rightmax = max(rightmax, height[r])
                water_trapped = max(0, rightmax - height[r])
                r-=1

            total_water+= water_trapped

        return total_water
                
        