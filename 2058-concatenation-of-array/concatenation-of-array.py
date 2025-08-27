class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k=0
        n=len(nums)
        while k < n:
            nums.append(nums[k])
            k+=1
        return nums