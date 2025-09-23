class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r= len(height)-1
        nums = height
        area = 0
        while l <r:
            w= r-l
        
            area = max(area, (w*min(nums[l] , nums[r])))
        
            if nums[l]<=nums[r]:
                l+=1
            elif nums[l]>=nums[r]:
                r-=1

        return area