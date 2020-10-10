#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (43.91%)
# Likes:    2010
# Dislikes: 241
# Total Accepted:    249.3K
# Total Submissions: 567.6K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#

# @lc code=start
class Solution:
    # dfs tle
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     def dfs(index,sumI,depth):
    #         if index < len(nums):
    #             sumI += nums[index]
    #             return min(dfs(index+depth,sumI,depth+1),dfs(index+depth+1,sumI,depth+1))
    #         else:
    #             return sumI

    #     nums = list(itertools.chain.from_iterable(triangle))
    #     minSum = float('inf')
    #     return dfs(0,0,1)

    # dp
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 
        res = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j],res[j+1])+triangle[i][j]
        return res[0]

    
        
# @lc code=end

