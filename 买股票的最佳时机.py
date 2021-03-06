"""
去寻找售出最大值和买进的最小值即可
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy = prices[0]
        sell = 0
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            sell = max(sell, prices[i] - buy)
        return sell
