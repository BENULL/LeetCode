#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (52.14%)
# Likes:    1491
# Dislikes: 110
# Total Accepted:    383.6K
# Total Submissions: 735.4K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows<1:
            return []
        for i in range(1,numRows):
            tmp = [0] + res[-1] + [0]
            new = [ tmp[index] + tmp[index-1] for index in range(1,len(tmp))]
            res.append(new)
        return res

        
# @lc code=end

