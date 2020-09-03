#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (31.59%)
# Likes:    4655
# Dislikes: 169
# Total Accepted:    360.2K
# Total Submissions: 1.1M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#

# @lc code=start
class Solution:
    # dp
    def maxProduct(self, nums: List[int]) -> int:
        maxPro = minPro = ans = nums[0]
        for i in range(1,len(nums)):
            x = max(nums[i],nums[i]*maxPro,nums[i]*minPro)
            y = min(nums[i],nums[i]*maxPro,nums[i]*minPro)
            maxPro,minPro = x,y
            ans = max(maxPro,ans)
        return ans
       
        
# @lc code=end

