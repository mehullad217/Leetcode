class Solution:
    def findLHS(self, nums: List[int]) -> int:

        l=0
        r=1

        nums.sort()
        longest=0
        while r<len(nums):
            if nums[r] - nums[l] ==1:
                longest = max(longest , r-l+1)
            else:
                while nums[r]-nums[l]>1:
                    l+=1
            r+=1

        return longest