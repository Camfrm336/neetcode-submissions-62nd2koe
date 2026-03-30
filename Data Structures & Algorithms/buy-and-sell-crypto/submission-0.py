class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            if profit > 0:
                maxProfit = max(profit, maxProfit)
            if prices[left] > prices[right]:
                left = right
        
        return maxProfit
