class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        memo ={0:0 ,1:0}
        def f(x):
            if x in memo:
                return memo[x]

            else:
                memo[x] = min(f(x-1)+cost[x-1] ,  f(x-2)+cost[x-2])

            return memo[x]

        return f(n)