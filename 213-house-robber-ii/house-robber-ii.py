class Solution:
    def rob(self, nums: List[int]) -> int:

        n= len(nums)
        if n==0:
            return 0

        if n==1:
            return nums[0]
        dp1 = [0]*n
        dp2 = [0]*n

        for i in range(n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        
        for i in range(1,n):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])


        return max(dp1[n-2] ,dp2[n-1])



