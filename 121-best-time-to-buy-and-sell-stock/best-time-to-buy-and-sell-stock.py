class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        l=0
        max_profit = 0

        for r in range (n):
            if prices[r] < prices[l]:
                l=r

            max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit






