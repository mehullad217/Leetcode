class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        output =[]
        count=0
        product=1
        while r<len(nums):
            product*=nums[r]

            while product>=k and l<=r:
                product=product/ nums[l]
                l+=1
            count+=r-l+1

            r+=1

        return count