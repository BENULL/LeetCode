#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#
# https://leetcode-cn.com/problems/total-hamming-distance/description/
#
# algorithms
# Medium (60.29%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    37.7K
# Total Submissions: 62.5K
# Testcase Example:  '[4,14,2]'
#
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
# 
# 给你一个整数数组 nums，请你计算并返回 nums 中任意两个数之间汉明距离的总和。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,14,2]
# 输出：6
# 解释：在二进制表示中，4 表示为 0100 ，14 表示为 1110 ，2表示为 0010 。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
# 2 + 2 = 6
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [4,14,4]
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        # TLE
        # @functools.lru_cache(None)
        # def hamming(x,y):
        #     xor = x ^ y
        #     distance = 0
        #     while xor:
        #         distance += 1
        #         # remove the rightmost bit of '1'
        #         xor = xor & (xor - 1)
        #     return distance

        # res = 0
        # for x, y in itertools.combinations(nums,2):
        #     res += hamming(x,y)
        # return res

        # 逐位计算
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans
        


# @lc code=end

