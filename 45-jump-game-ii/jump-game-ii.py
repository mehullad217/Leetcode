class Solution:
    def jump(self, nums: List[int]) -> int:
        n= len(nums)
        max_covered =0
        furthest= 0 
        i=0
        jumps=0
        while max_covered <n-1:
            while i<=max_covered:
                furthest = max(furthest , i+nums[i])
                i+=1

            jumps+=1
            max_covered= max(max_covered, furthest)

        return jumps





        