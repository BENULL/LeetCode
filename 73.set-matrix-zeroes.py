#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (43.01%)
# Likes:    2436
# Dislikes: 326
# Total Accepted:    340.1K
# Total Submissions: 785.2K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given an m x n matrix. If an element is 0, set its entire row and column to
# 0. Do it in-place.
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rowSet = colSet = False
        for i,j in itertools.product(range(rows),range(cols)):
            if matrix[i][j] == 0:
                if i == 0:
                    rowSet = True
                if j == 0:
                    colSet = True
                matrix[0][j] = matrix[i][0] = 0

        for j in range(1,cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0

        for i in range(1,rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        if rowSet:
            for j in range(cols):
                    matrix[0][j] = 0
        if colSet:
            for i in range(rows):
                    matrix[i][0] = 0
        


                



        
# @lc code=end

