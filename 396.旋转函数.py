#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#
# https://leetcode-cn.com/problems/rotate-function/description/
#
# algorithms
# Medium (41.25%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    7.9K
# Total Submissions: 19K
# Testcase Example:  '[4,3,2,6]'
#
# 给定一个长度为 n 的整数数组 A 。
# 
# 假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：
# 
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。
# 
# 计算F(0), F(1), ..., F(n-1)中的最大值。
# 
# 注意:
# 可以认为 n 的值小于 10^5。
# 
# 示例:
# 
# 
# A = [4, 3, 2, 6]
# 
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
# 
# 所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
# 
# 
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # brute for TLE
        # n = len(nums)
        # return max(sum(index*num for index,num in enumerate(nums[i:]+nums[:i])) for i in range(n,0,-1))

        # math
        # F(k) = 0 * B(k-1)[n-1] + 1 * B(k-1)[0] + 2 * B(k-1)[1] + ... + (n-1) * B(k-1)[n-2]
        #     = F(k-1) + B(k-1)[0] + B(k-1)[1] + ... + B(k-1)[n - 2] - (n - 1) * B(k-1)[n - 1]
        #     = F(k-1) + sum(B(k-1)) - n * B(0)[n - k]
        #     = F(k-1) + sum(A) - n * B(0)[n - k]
        n = len(nums)
        _sum = sum(nums)
        prev = sum(index*nums[index] for index in range(n))

        res = prev
        for k in range(1,n):
            sums = prev + _sum - n*nums[n-k]
            res = max(res, sums)
            prev = sums
        return res

        




# @lc code=end

