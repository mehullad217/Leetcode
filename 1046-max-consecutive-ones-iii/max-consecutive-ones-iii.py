class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        count=0
        max_count = 0
        while r<len(nums):
            if nums[r] ==0:
                count+=1
            while count>k:
                if nums[l]==0:
                    count-=1
                l+=1
        

            max_count = max(max_count,r-l+1)
            r+=1

        return max_count