#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#
# https://leetcode-cn.com/problems/nth-digit/description/
#
# algorithms
# Medium (40.66%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    16.3K
# Total Submissions: 40.1K
# Testcase Example:  '3'
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。
# 
# 
# 
# 注意：n 是正数且在 32 位整数范围内（n < 2^31）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：3
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
# 
# 
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        
         count = 9
         len = 1
         start = 1
         while (n > len * count) :
             n -= len * count
             len += 1
             count *= 10
             start *= 10

         start += (n - 1) / len # find the number
         num = str(start)

         return int(num[(n - 1) % len]) 
# @lc code=end

