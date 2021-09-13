#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#
# https://leetcode-cn.com/problems/non-decreasing-array/description/
#
# algorithms
# Medium (27.03%)
# Likes:    610
# Dislikes: 0
# Total Accepted:    73.8K
# Total Submissions: 273.1K
# Testcase Example:  '[4,2,3]'
#
# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
# 
# 我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 ，总满足 nums[i] 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# - 10 ^ 5 
# 
# 
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # changes = 0
        # _max = - 10**5 -1
        # for i in range(1, len(nums)):
        #     if nums[i]<nums[i-1]:
        #         changes += 1
        #         if changes>1: return False

        #         if min(nums[i], nums[i-1])>=_max:
        #             nums[i] = nums[i-1] = min(nums[i], nums[i-1])
        #         else:
        #             nums[i] = nums[i-1]
        #     _max = nums[i-1]

        # return True

        N = len(nums)
        count = 0
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                count += 1
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return count <= 1

# https://leetcode-cn.com/problems/non-decreasing-array/solution/3-zhang-dong-tu-bang-zhu-ni-li-jie-zhe-d-06gi/

# @lc code=end

