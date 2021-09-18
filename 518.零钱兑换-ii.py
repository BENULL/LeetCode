#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (65.31%)
# Likes:    606
# Dislikes: 0
# Total Accepted:    104.7K
# Total Submissions: 160K
# Testcase Example:  '5\n[1,2,5]'
#
# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
# 
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
# 
# 假设每一种面额的硬币有无限个。 
# 
# 题目数据保证结果符合 32 位带符号整数。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：amount = 5, coins = [1, 2, 5]
# 输出：4
# 解释：有四种方式可以凑成总金额：
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# 示例 2：
# 
# 
# 输入：amount = 3, coins = [2]
# 输出：0
# 解释：只用面额 2 的硬币不能凑成总金额 3 。
# 
# 
# 示例 3：
# 
# 
# 输入：amount = 10, coins = [10] 
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# coins 中的所有值 互不相同
# 0 
# 
# 
#

# @lc code=start


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # different between permutation and combination 

        """
        wrong answer 
        permutation as behind but we need combination
        from up to bottom 
        """
        # def count(amount):
        #     if amount==0: return 1
        #     return sum([count(amount-coin) for coin in coins if amount>=coin])
        # return count(amount)

        """
        combination
        from bottom to up
        2d dp
        """
        # I = len(coins)+1
        # J = amount+1
        # dp = [[0]*J for _ in range(I)]
        # # base case
        # dp[0][0] = 1 
        # for c in range(1, I):
        #     dp[c][0] = 1
        #     for a in range(1, J):
        #         dp[c][a] = dp[c-1][a] + (dp[c][a-coins[c-1]] if a>=coins[c-1] else 0)
        # return dp[I-1][J-1]

        """
        combination
        from bottom to up
        1d dp
        """
        J = amount+1
        dp = [0]*J 
        # base case
        dp[0] = 1 
        for coin in coins:
            for a in range(1, J):
                if a>=coin:
                    dp[a] += dp[a-coin]
        return dp[J-1]

        """
        combination
        from up to bottom 
        """
        # I = len(coins)
        # @functools.lru_cache(None)
        # def count(j, i):
        #     if j==0: return 1
        #     if i<0: return 0
        #     return count(j,i-1)+(count(j-coins[i], i) if j>=coins[i] else 0)
        # return count(amount,I-1)

# @lc code=end

