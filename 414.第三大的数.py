#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# https://leetcode-cn.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (35.80%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    48.3K
# Total Submissions: 134.8K
# Testcase Example:  '[3,2,1]'
#
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[3, 2, 1]
# 输出：1
# 解释：第三大的数是 1 。
# 
# 示例 2：
# 
# 
# 输入：[1, 2]
# 输出：2
# 解释：第三大的数不存在, 所以返回最大的数 2 。
# 
# 
# 示例 3：
# 
# 
# 输入：[2, 2, 3, 1]
# 输出：1
# 解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
# 此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
# 
# 
# 
# 提示：
# 
# 
# 1 
# -2^31 
# 
# 
# 
# 
# 进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？
# 
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums = sorted(list(set(nums)))
        # return nums[-1] if len(nums) <= 2 else nums[-3]

        first = second = third = float('-inf')
        for num in nums:
            if num > third:  # 通过第3关
                if num < second:
                    third = num
                elif num > second:  # 通过第2关
                    if num < first:
                        third = second
                        second = num
                    elif num > first:  # 通过第1关
                        third = second
                        second = first
                        first = num
        if third == float('-inf'):
            return first
        else:
            return third
# @lc code=end

