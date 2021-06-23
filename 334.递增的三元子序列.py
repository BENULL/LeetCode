#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
# https://leetcode-cn.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (41.41%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    37.6K
# Total Submissions: 90.7K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
# 
# 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true
# ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,4,5]
# 输出：true
# 解释：任何 i < j < k 的三元组都满足题意
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,4,3,2,1]
# 输出：false
# 解释：不存在满足题意的三元组
# 
# 示例 3：
# 
# 
# 输入：nums = [2,1,5,0,4,6]
# 输出：true
# 解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
# 
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
# 进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？
# 
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # if len(nums)<3: return False
        # a, b= 0xffffffff, 0xffffffff
        # for n in nums:
        #     if n <= a: 
        #         a = n
        #     elif n <= b:
        #         b = n
        #     else:
        #         return True
        # return False

        small, mid = float('inf'), float('inf')
        for x in nums:
            if x <= small:
                small = x
            elif x <= mid:
                mid = x
            elif x > mid:
                return True 
        return False





# @lc code=end

