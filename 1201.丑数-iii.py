#
# @lc app=leetcode.cn id=1201 lang=python3
#
# [1201] 丑数 III
#
# https://leetcode-cn.com/problems/ugly-number-iii/description/
#
# algorithms
# Medium (24.83%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 25.2K
# Testcase Example:  '3\n2\n3\n5'
#
# 给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。
# 
# 丑数是可以被 a 或 b 或 c 整除的 正整数 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3, a = 2, b = 3, c = 5
# 输出：4
# 解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
# 
# 示例 2：
# 
# 
# 输入：n = 4, a = 2, b = 3, c = 4
# 输出：6
# 解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
# 
# 
# 示例 3：
# 
# 
# 输入：n = 5, a = 2, b = 11, c = 13
# 输出：10
# 解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
# 
# 
# 示例 4：
# 
# 
# 输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
# 输出：1999999984
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 本题结果在 [1, 2 * 10^9] 的范围内
# 
# 
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # binary search + inclusion-exclusion principle
        lab, lac, lbc, labc = lcm(a,b), lcm(a,c), lcm(b,c), lcm(a, b, c)
        def uglys(x):
            return x//a + x//b + x//c - x//lab - x//lbc - x//lac + x//labc
        left, right = 1, min(min(a, b, c) * n, 2 * pow(10, 9)) 
        while left<right:
            mid = left + (right - left) // 2
            if uglys(mid)<n:
                left = mid + 1
            else:
                right = mid
        return left            
# @lc code=end

