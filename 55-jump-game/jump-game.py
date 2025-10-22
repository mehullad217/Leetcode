class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        farthest=0
        for i in range(len(nums)):
            if i<=farthest:
                farthest =  max(farthest,i+ nums[i])

        if farthest >= len(nums)-1:
            return True
        else:
            return False
        