#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.43%)
# Likes:    1211
# Dislikes: 0
# Total Accepted:    335.2K
# Total Submissions: 790.8K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 
# 进阶：
# 
# 
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 
# 示例 2：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 
# 示例 3：
# 
# 
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# nums 是一个非递减数组
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # use bisect

        # if not nums:
        #     return [-1, -1]
        # x, y = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        # x = x if x < len(nums) and nums[x] == target else -1
        # y = y - 1 if y > 0 and x < len(nums) and nums[x] == target else -1
        # return [x, y]

        # binary search
        def lower_bound(nums, target):
            left, right = 0, len(nums)-1
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid]>=target:
                    right = mid - 1 
                else:
                    left = mid + 1
            return left

        def upper_bound(nums, target):
            left, right = 0, len(nums)-1
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid]<=target:
                    left = mid + 1 
                else:
                    right = mid - 1
            return right
        
        if not nums:
            return [-1, -1]
        
        lower = lower_bound(nums, target)
        if lower==len(nums) or nums[lower]!=target:
            return [-1, -1]
        upper = upper_bound(nums, target)
        return [lower, upper]

# @lc code=end

