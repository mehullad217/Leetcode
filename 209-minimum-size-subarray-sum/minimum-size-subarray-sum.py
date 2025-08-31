class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        min_length = float('inf')
        sum1= 0
        while r< len(nums):
            if l==r and nums[r] >= target:
                return (1)
            
            sum1+=nums[r]
            #print('Initial sum1' , sum1)

            while sum1>= target:

                min_length = min(min_length, len(nums[l:r+1]))
                # print('Value of r' ,r)
                # print('target subarray' , nums[l:r+1])
                # print('Current subarray length' , len(nums[l:r+1]))
                # print('Min_len of Target so far' ,  min_length )

                sum1-=nums[l]
                # print('Sum1 after shrinking l' ,  sum1 )
                l+=1
            r+=1
        return 0 if min_length == float('inf') else min_length