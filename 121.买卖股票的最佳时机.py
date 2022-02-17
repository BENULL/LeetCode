#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (57.46%)
# Likes:    2118
# Dislikes: 0
# Total Accepted:    669.5K
# Total Submissions: 1.2M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 
# 
# 示例 2：
# 
# 
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force

        # minPrice = float('inf')
        # maxProfit = 0
        # for price in prices:
        #     minPrice = min(minPrice, price)
        #     maxProfit = max(maxProfit, price-minPrice)
        # return maxProfit
        

        # dp 等同 brute force

        # n = len(prices)

        # # dp[i] 到i为止的minPince

        # dp = [0]*n 
        # dp[0] = prices[0]
        # maxProfit = 0
        # for i in range(1,n):
        #     dp[i] = dp[i - 1] if (dp[i - 1] < prices[i]) else prices[i]
        #     maxProfit = max(prices[i] - dp[i], maxProfit)
        # return maxProfit


        # dp 买卖股票通用
        n = len(prices)
        """
        https://mp.weixin.qq.com/s/hvaTYIz73xjR0_Kqel2mgw
        dp[i][k][state] 
        state: buy, sell, no operate 1表示持有 0表示没持有
        k: 交易次数
        i: 第i天的状态
        """

        """
        当前k==1
        状态转移方程
        dp[i][k][0] = max(dp[i-1][k][1]+prices[i], dp[i-1][k][0])
        dp[i][k][1] = max(dp[i-1][k-1][0]-prices[i], dp[i-1][k][1])
        """
        # dp = [[0]*2 for _ in range(n)]
        # for i in range(n):
        #     if i-1 == -1:
        #         dp[i][0] = 0
        #         dp[i][1] = -prices[i]
        #         continue
        #     dp[i][0] = max(dp[i-1][1]+prices[i], dp[i-1][0])
        #     dp[i][1] = max(-prices[i], dp[i-1][1])
        # return dp[n-1][0]

        # 优化空间
        # base case

        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

# @lc code=end

