#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (46.45%)
# Likes:    3011
# Dislikes: 121
# Total Accepted:    183.7K
# Total Submissions: 398.5K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.
# 
# Example 1:
# 
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Constraints:
# 
# 
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#

# @lc code=start
class Solution:
    
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #    # dfs + memo
    #     def findTarget(i,s):
    #         if (i,s) not in cache:
    #             r = 0
    #             if i == len(nums):
    #                 if s == 0:
    #                     r = 1
    #             else:
    #                 r = findTarget(i+1,s-nums[i])+findTarget(i+1,s+nums[i])
    #             cache[(i,s)] = r
            
    #         return cache[(i,s)]

            
    #     cache = {}
    #     return findTarget(0,S)


        # dp 背包方案数
        n = len(nums)
        _sum = sum(nums)
        if abs(S) > _sum:
            return 0
        dp = [[0]*(2*_sum+1) for _ in range(n+1)]
        # dp[i][j] 表示 使用i个num 和为j 的方案数
        # dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j+nums[i-1]]

        # base case
        dp[0][0+_sum] = 1

        for i in range(1,n+1):
            for j in range(-_sum, _sum+1):
                if (j - nums[i-1]) + _sum >= 0:
                    dp[i][j + _sum] += dp[i - 1][(j - nums[i-1]) + _sum]
                if (j + nums[i-1]) + _sum <= 2 * _sum:
                    dp[i][j + _sum] += dp[i - 1][(j + nums[i-1]) + _sum]
        return dp[n][_sum+S]
        

        
# @lc code=end

