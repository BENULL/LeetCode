#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (44.74%)
# Likes:    226
# Dislikes: 0
# Total Accepted:    71.8K
# Total Submissions: 160.6K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
# 
# 请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
# 
# 任何误差小于 10^-5 的答案都将被视为正确答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,12,-5,-6,50,3], k = 4
# 输出：12.75
# 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5], k = 1
# 输出：5.00000
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= k <= n <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum = 0
        start, end = 0, 0
        max_avg = float('-inf')
        while start <= len(nums)- k:
            if end - start  < k:
                _sum += nums[end]
                end += 1
            elif end - start == k:
                max_avg = max(max_avg, _sum/k)
                _sum -= nums[start]
                start += 1
        return max_avg
            
            
            
# @lc code=end

