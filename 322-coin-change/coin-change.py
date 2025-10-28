class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount ==0:
            return 0
        dp  = [0]*(amount+1)

        dp[0] = 0

        for i in range(1,amount+1):
            minn = float('inf')
            for j in coins:
                if i-j>=0:
                    minn = min(minn, 1+ dp[i-j])

            dp[i]=minn
        
        
        if dp[amount]<float('inf'):
            return dp[amount]
        else:
            return -1






        
   
            





        