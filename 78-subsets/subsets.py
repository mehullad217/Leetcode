class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol, res = [],[]
        n=len(nums)

        def backtrack(i):
            if i==n:
                sol.append(res[:])
                return

            #do not include
            backtrack(i+1)
            res.append(nums[i])
            backtrack(i+1)
            res.pop()
        
        backtrack(0)
        
        return sol