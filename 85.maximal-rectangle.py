#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (37.51%)
# Likes:    4019
# Dislikes: 86
# Total Accepted:    220.7K
# Total Submissions: 557.2K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest
# rectangle containing only 1's and return its area.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# 
# 
# Example 2:
# 
# 
# Input: matrix = []
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: matrix = [["0"]]
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: matrix = [["1"]]
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: matrix = [["0","0"]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# rows == matrix.length
# cols == matrix[i].length
# 0 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    """ The solution is based on largest rectangle in histogram solution.
        Every row in the matrix is viewed as the ground with some buildings on it. The building height is the count of consecutive 1s from that row to above rows. 
        The rest is then the same as this solution for largest rectangle in histogram
    """

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        h, w = len(matrix), len(matrix[0])
        m = [[0]*w for _ in range(h)]
        for j,i in itertools.product(range(h),range(w)):
            if matrix[j][i]== '1':
                m[j][i] = m[j-1][i] + 1
        return max(self.largestRectangleArea(row) for row in m)

    def largestRectangleArea(self,height):
        height.append(0)
        stack, size = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]]>height[i]:
                h = height[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                size = max(size,h*w)
            stack.append(i)
        return size      
# @lc code=end

