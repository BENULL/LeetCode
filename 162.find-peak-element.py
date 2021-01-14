#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (43.22%)
# Likes:    2399
# Dislikes: 2431
# Total Accepted:    442.4K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is strictly greater than its neighbors.
# 
# Given an integer array nums, find a peak element, and return its index. If
# the array contains multiple peaks, return the index to any of the peaks.
# 
# You may imagine that nums[-1] = nums[n] = -∞.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# 
# Example 2:
# 
# 
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
# 
# 
# 
# Follow up: Could you implement a solution with logarithmic complexity?
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            midL = left + (right-left)//2
            midR = midL + 1
            if nums[midL]<nums[midR]:
                left = midL + 1
            else:
                right  = midL
        return left

        
# @lc code=end

