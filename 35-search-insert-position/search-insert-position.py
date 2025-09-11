class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r= len(nums)-1
        while l<=r:
            middle = l+((r-l)//2)

            if nums[middle]==target:
                return (middle)

            elif nums[middle]<target:
                l=middle+1
            else:
                r=middle-1


        if target > nums[middle]:
            return (middle+1)
        elif target <nums[middle]:
            return (middle) 