#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
# https://leetcode-cn.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (57.60%)
# Likes:    390
# Dislikes: 0
# Total Accepted:    48.3K
# Total Submissions: 83.8K
# Testcase Example:  '1\n2'
#
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
# 
# 示例 1:
# 
# 输入: a = 1, b = 2
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: a = -2, b = 3
# 输出: 1
# 
#

# @lc code=start
class Solution:
    # python 无限长int 处理
    # https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/
    def getSum(self, a: int, b: int) -> int:
        mask = 0x100000000
        max_int = 0x7FFFFFFF
        min_int = max_int + 1
        while b!=0:
            carry = (a&b) << 1
            a = (a^b) % mask
            b = carry % mask
        return a if a <= max_int else ~((a % min_int) ^ max_int) 



# @lc code=end

