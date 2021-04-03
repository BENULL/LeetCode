#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (50.14%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    42.5K
# Total Submissions: 84.7K
# Testcase Example:  '16'
#
# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
# 
# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 16
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：n = 5
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：n = 1
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# 
# 
# 
# 
# 进阶：
# 
# 
# 你能不使用循环或者递归来完成本题吗？
# 
# 
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 数是否为 2 的幂：x > 0 and x & (x - 1) == 0

        # Solution 1: brute force + memo
        # return n in [4**i for i in range(16)]

        # Solution 2: math
        # check if log2(x) is odd
        # return n > 0 and math.log2(n)%2 == 0 

        # Solution 3: math
        # 若 x 为 2 的幂且 x%3 == 1，则 x 为 4 的幂

        return n > 0 and n & (n - 1) == 0 and n % 3 == 1



        


# @lc code=end

