#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (46.39%)
# Likes:    3042
# Dislikes: 95
# Total Accepted:    169.2K
# Total Submissions: 354.5K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
# 
# 
# Example:
# 
# 
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) <=1:
        #     return 0
        # 卖出 买入 模拟dp
        # dp = [[None,None] for _ in range(len(prices))]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # dp[1][0] = max(dp[0][0],dp[0][1]+prices[1])
        # dp[1][1] = max(dp[0][1],dp[0][0]-prices[1])
        # for i in range(2,len(prices)):
        #     dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        #     dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
        # return dp[-1][0]

        # Recursive

        @lru_cache(None)
        def maxProfit(i,bought = False,buyValue = None):
            if i>=len(prices):
                return 0
            if not bought:
                # Buy or leave the stock
                return max(maxProfit(i+1,True,prices[i]),maxProfit(i+1,False))
            if bought:
                # Sell the stock and jump 2 day ahead (cooldown period) or retain the stock
                return max((prices[i]-buyValue)+maxProfit(i+2,False,0),maxProfit(i+1,True,buyValue))
        return maxProfit(0)
    
# @lc code=end