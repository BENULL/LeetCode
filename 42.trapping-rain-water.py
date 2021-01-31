#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (48.59%)
# Likes:    9714
# Dislikes: 148
# Total Accepted:    661.8K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    # def trap(self, height: List[int]) -> int:
    #     if not height:
    #         return 0
    #     index = height.index(max(height))
    #     return self.helper(height[:index+1])+self.helper(height[:index-len(height)-1:-1])

        
    # def helper(self,height):
    #     res = 0
    #     if len(height)<3:
    #         return res
    #     i = 0
    #     while i < len(height)-1:
    #         if height[i]>0:
    #             firstMaxIndex = i + 1
    #             while firstMaxIndex <len(height) and height[firstMaxIndex]<height[i]:
    #                 firstMaxIndex += 1
    #             if firstMaxIndex <len(height):
    #                 res += (min(height[i],height[firstMaxIndex])*(firstMaxIndex-i-1))-sum(height[i+1:firstMaxIndex])
    #                 i = firstMaxIndex
    #             else:
    #                 i += 1
    #         else:
    #             i += 1
    #     return res


    # two pointer
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        leftMax, rightMax = 0, 0 
        while left < right:
            if height[left]<height[right]:
                if height[left]>=leftMax:
                    leftMax = height[left]
                else:
                    res += leftMax-height[left]
                left += 1
            else:
                if height[right]>=rightMax:
                    rightMax = height[right]
                else:
                    res += rightMax-height[right]
                right -= 1
        return res
        
# @lc code=end

