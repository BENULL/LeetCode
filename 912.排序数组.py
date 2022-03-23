#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (55.60%)
# Likes:    502
# Dislikes: 0
# Total Accepted:    320.2K
# Total Submissions: 576.1K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
# 
# 
#

# @lc code=start
import random


class Solution:
    # quick sort
    def sortArray(self, nums):
        random.shuffle(nums)
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, i, j):
        if i>=j:
            return 
        pivot_idx = self.partition(nums, i, j)
        self.quickSort(nums, i, pivot_idx-1)
        self.quickSort(nums, pivot_idx+1, j)
       
    def partition(self, nums, i, j):
        pivot = nums[i]
        left, right = i+1, j
        while left<=right:
            while left<j and nums[left]<=pivot:
                left += 1
            while right>i and nums[right]>pivot:
                right -= 1
            if left>=right:
                break
            nums[left], nums[right] = nums[right], nums[left] 
        nums[i], nums[right] = nums[right], nums[i]
        return right

# if __name__ == '__main__':
#     s = Solution()
#     s.sortArray([5,2,3,1])

# @lc code=end

