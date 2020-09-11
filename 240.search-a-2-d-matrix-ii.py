#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (43.07%)
# Likes:    3483
# Dislikes: 78
# Total Accepted:    344.1K
# Total Submissions: 795.1K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
#'5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# Example:
# 
# Consider the following matrix:
# 
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# Given target = 5, return true.
# 
# Given target = 20, return false.
# 
#

# @lc code=start
class Solution:
  """
  Starting from Top-Right corner:
  If current grid M[r][c] is smaller than target x, there is no need to consider M[r][ :c] since all the grids on the left must be smaller as well. So, x must be in the rows below and we can safely make r += 1.
  We keep moving M[r][c] downwards until it's larger x, then we can safely move leftwards and make c -= 1 since all the grids in M[ :r][c ] would be larger than x.
  During the search, if x is found, we return True. Otherwise, we can either move downwards or leftwards safely.
  If we reach left-bottom corner without hitting x, then target is not in the matrix.
  """
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m,n = len(matrix),len(matrix) and len(matrix[0])
    r,c = 0,n-1
    while r<m and c>=0:
      if matrix[r][c]<target:
        r+=1
      elif matrix[r][c]>target:
        c-=1
      else:
        return True

    return False


        
# @lc code=end

