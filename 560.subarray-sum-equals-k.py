#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.86%)
# Likes:    5528
# Dislikes: 178
# Total Accepted:    368.9K
# Total Submissions: 842.2K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
#

# @lc code=start
class Solution:
    # for bruce we need sum[i,j] the time complexity is O(n^2)  it will TLE
    # so we can memory the preSum use dict
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = res = 0
        _dict = collections.defaultdict(int)
        for num in nums:
            total += num
            if total-k in _dict:
                res += _dict[total-k]
            if total == k:
                res += 1
            _dict[total] += 1
        return res
        
# @lc code=end

