#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (47.14%)
# Likes:    3154
# Dislikes: 194
# Total Accepted:    321.2K
# Total Submissions: 677.7K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

# @lc code=start
class Solution:
    # dp
    def numSquares(self, n: int) -> int:
        dp = [0]
        while len(dp)<=n:
            m = len(dp)
            ans = sys.maxsize
            for i in range(1,int(math.sqrt(m))+1):
                if i*i <= m:
                    ans = min(ans,dp[m-i*i]+1)
            dp.append(ans)
        return dp[n]
        
# @lc code=end

