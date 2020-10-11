#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (38.29%)
# Likes:    1175
# Dislikes: 189
# Total Accepted:    127.8K
# Total Submissions: 325.1K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
# 
# 
# 
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
# and (row2, col2) = (4, 3), which contains sum = 8.
# 
# 
# Example:
# 
# Given matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# 
# 
# Note:
# 
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
# 
# 
#

# @lc code=start
class NumMatrix:
  # ---------------------------
  # |                         |
  # |           (r1,c1)       |
  # |             |-----------|(r1,c2)
  # |             |  RegionA  |
  # | ------------------------|(r2,c2)
  # |           (r2,c1)       |
  #  --------------------------
  #  RegionA = region(0,0 to r2,c2) - 
  #       region(0,0 to r2,c1) - 
  #       region(0,0 to r1,c2) + 
  #       region(0,0 to r1,c1)

    def __init__(self, matrix: List[List[int]]):
      if not matrix:
        return
      n,m = len(matrix),len(matrix[0])
      self.dp = [[0]*(m+1) for _ in range(n+1)]
      for i,j in itertools.product(range(n),range(m)):
        self.dp[i+1][j+1] = matrix[i][j]+self.dp[i+1][j]+self.dp[i][j+1]-self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
      return self.dp[row2+1][col2+1]-self.dp[row1][col2+1]-self.dp[row2+1][col1]+self.dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

