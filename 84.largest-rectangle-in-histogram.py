#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (34.92%)
# Likes:    5504
# Dislikes: 111
# Total Accepted:    348.2K
# Total Submissions: 932.7K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
# 
# 
# Example 1:
# 
# 
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
# 
# 
# Example 2:
# 
# 
# Input: heights = [2,4]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    # similiar with 85.
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack, size = [], 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                size = max(size,h*w)
            stack.append(i)
        return size    
        
# @lc code=end

