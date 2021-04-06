#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (52.08%)
# Likes:    349
# Dislikes: 0
# Total Accepted:    106.5K
# Total Submissions: 204.5K
# Testcase Example:  '"11"\n"123"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 
# 
# 提示：
# 
# 
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # built
        # return (str(eval(num1+'+'+num2)))

        result = []
        carry = 0
        for i, j in zip_longest(reversed(num1), reversed(num2), fillvalue=0):
            carry, curr = divmod(int(i)+int(j)+carry, 10)
            result.append(str(curr))
        if carry:
            result.append(str(carry))
        return "".join(reversed(result))
# @lc code=end

