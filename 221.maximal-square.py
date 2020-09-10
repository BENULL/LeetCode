#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (37.61%)
# Likes:    3392
# Dislikes: 88
# Total Accepted:    283.6K
# Total Submissions: 749.1K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#

# @lc code=start
class Solution:
    # dp
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if  matrix is None or len(matrix)<1:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [ [0]*(cols+1) for _ in range(rows+1)]
        maxSide = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c],dp[r+1][c],dp[r][c+1]) + 1
                    maxSide = max(maxSide,dp[r+1][c+1])
        return maxSide*maxSide




        
# @lc code=end

