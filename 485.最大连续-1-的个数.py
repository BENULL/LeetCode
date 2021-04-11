#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (59.93%)
# Likes:    226
# Dislikes: 0
# Total Accepted:    101.6K
# Total Submissions: 169.7K
# Testcase Example:  '[1,1,0,1,1,1]'
#
# 给定一个二进制数组， 计算其中最大连续 1 的个数。
# 
# 
# 
# 示例：
# 
# 
# 输入：[1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
# 
# 
# 
# 
# 提示：
# 
# 
# 输入的数组只包含 0 和 1 。
# 输入数组的长度是正整数，且不超过 10,000。
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # res = 0
        # if not nums: return res
        # i = j = 0
        # while j < len(nums):
        #     if nums[i]==1 and nums[j]==1:
        #         res = max(res,j-i+1)
        #         j += 1
        #     else:
        #         i = j+1
        #         j = i
        # return res

        # index = -1
        # res = 0
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         index = i
        #     else:
        #         res = max(res, i - index)
        # return res

        return max([len(list(lst)) for e, lst in groupby(nums) if e == 1]+[0])







        
# @lc code=end

