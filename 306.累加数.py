#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
# https://leetcode-cn.com/problems/additive-number/description/
#
# algorithms
# Medium (33.55%)
# Likes:    165
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 43.3K
# Testcase Example:  '"112358"'
#
# 累加数是一个字符串，组成它的数字可以形成累加序列。
# 
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
# 
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
# 
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
# 
# 示例 1:
# 
# 输入: "112358"
# 输出: true 
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# 
# 示例 2:
# 
# 输入: "199100199"
# 输出: true 
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
# 
# 进阶:
# 你如何处理一个溢出的过大的整数输入?
# 
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # backtrace

        n = len(num)
        if n < 3:
            return False

        def check(p1, p2, j):
            while j < n:
                # python 无溢出
                p = str(int(p1) + int(p2))
                if num[j: j+len(p)] != p:
                    return False
                j += len(p)
                p1, p2 = p2, p
            return True


        for i in range(1, n//2+1) if num[0] != "0" else [1]:
            for j in range(i+1, n) if num[i] != "0" else [i+1]:
                p1 = num[:i]
                p2 = num[i:j]
                if check(p1, p2, j):
                    return True

        return False

# @lc code=end

