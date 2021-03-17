#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (37.60%)
# Likes:    1253
# Dislikes: 1360
# Total Accepted:    323.5K
# Total Submissions: 835.9K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # memo = collections.defaultdict(lambda:-1)
        # for i,n in enumerate(nums):
        #     if memo[n]>-1 and abs(i-memo[n]) <= k:
        #         return True
        #     else:
        #         memo[n] = i
        # return False

        if len(nums) == len(set(nums)):
            return False

        if len(nums) <= k + 1:  # k is big enough to cover the whole list
            return True

        for i in range(len(nums) - k):
            if len(nums[i:(i + k + 1)]) != len(set(nums[i:(i + k + 1)])):
                return True

        return False


        
# @lc code=end

