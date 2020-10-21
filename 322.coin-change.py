#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (35.22%)
# Likes:    5173
# Dislikes: 158
# Total Accepted:    487.9K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: coins = [1], amount = 1
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: coins = [1], amount = 2
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp bottom to up
        # dp = [0] * (amount+1)
        # for i in range(1,amount+1):
        #     res = [dp[i-c]+1 for c in coins if i>=c and dp[i-c]>=0]
        #     if res:
        #         dp[i] = min(res)
        #     else:
        #         dp[i] = -1    
        # return dp[amount]

        # dp up to bottom
        # @lru_cache(None)
        # def count(amount):

        #     if amount==0: return 0
        #     res =  [count(amount-c) for c in coins if amount>=c]
        #     res = list(map(lambda y: y+1 ,filter(lambda x: x>=0, res)))

        #     if res:
        #         return min(res)
        #     else:
        #         return -1

        # return count(amount)
        



        
# @lc code=end

