#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
# https://leetcode-cn.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (27.54%)
# Likes:    381
# Dislikes: 0
# Total Accepted:    70.9K
# Total Submissions: 257.5K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
# 
# 
# 子数组大小 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 
# 
# 如果存在，返回 true ；否则，返回 false 。
# 
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
# 
# 示例 2：
# 
# 
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # TLE brute force
        # pre_sum = [0]
        # for i in range(len(nums)):
        #     pre_sum.append(nums[i]+pre_sum[i])
        # for i in range(2,len(nums)+1):
        #     for j in range(i-1):
        #         if (pre_sum[i]-pre_sum[j]) % k == 0:
        #             return True
        # return False

        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(nums[i]+pre_sum[i])
        rem_set= set()
        for i in range(2,len(nums)+1):
            rem_set.add(pre_sum[i-2]%k)
            if pre_sum[i]%k in rem_set:
                    return True
        return False




# @lc code=end

